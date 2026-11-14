cmake_minimum_required(VERSION 3.24)

project(veyra VERSION 2.1.5 LANGUAGES C CXX RC)
# Moonlight/Xbox have C sources independently of the optional PS5 backend.
# Shown in the EXE's version resource and in the package name. CMake versions
# must be numeric, so the beta marker lives here instead.
set(VEYRA_DISPLAY_VERSION "2.1.5" CACHE STRING "Human-readable version string")
# The cache keeps the first value it ever saw, so a release that bumps
# project(VERSION) used to ship an EXE still stamped with the previous display
# string. Re-align it whenever the cached label does not start with the project
# version; an explicit matching label (e.g. "1.4.0beta") is still honoured.
if(NOT VEYRA_DISPLAY_VERSION MATCHES "^${PROJECT_VERSION}")
  message(STATUS "VEYRA_DISPLAY_VERSION ${VEYRA_DISPLAY_VERSION} does not match project ${PROJECT_VERSION}; using ${PROJECT_VERSION}")
  set(VEYRA_DISPLAY_VERSION "${PROJECT_VERSION}" CACHE STRING "Human-readable version string" FORCE)
endif()

# Match the compiler's actual bytes, including on localized Windows installs.
# CMake's cached, decoded prefix can leave Ninja with zero header dependencies.
if(MSVC AND CMAKE_GENERATOR MATCHES "Ninja")
  set(VEYRA_INCLUDE_PROBE "${CMAKE_CURRENT_BINARY_DIR}/CMakeFiles/veyra-include-probe")
  file(WRITE "${VEYRA_INCLUDE_PROBE}.h" "// Dependency parser probe\n")
  file(WRITE "${VEYRA_INCLUDE_PROBE}.cpp" "#include \"veyra-include-probe.h\"\n")
  execute_process(COMMAND "${CMAKE_CXX_COMPILER}" /nologo /utf-8 /showIncludes /c /TP "${VEYRA_INCLUDE_PROBE}.cpp" "/Fo${VEYRA_INCLUDE_PROBE}.obj"
    OUTPUT_VARIABLE VEYRA_INCLUDE_OUTPUT ERROR_VARIABLE VEYRA_INCLUDE_OUTPUT
    RESULT_VARIABLE VEYRA_INCLUDE_RESULT ENCODING NONE)
  if(NOT VEYRA_INCLUDE_RESULT EQUAL 0 OR NOT VEYRA_INCLUDE_OUTPUT MATCHES "(^|[\r\n])([^\r\n]*: )[ ]*[A-Za-z]:[^\r\n]*veyra-include-probe.h")
    message(FATAL_ERROR "Unable to verify MSVC/Ninja header dependency prefix")
  endif()
  set(CMAKE_CL_SHOWINCLUDES_PREFIX "${CMAKE_MATCH_2}")
endif()

# ---------------------------------------------------------------------------
# Veyra cache variables and feature switches (Playbook section 5.1).
# Machine-specific absolute paths are resolved by scripts/build.ps1 at
# configure time; CMakePresets.json stays free of local paths.
# ---------------------------------------------------------------------------
set(VEYRA_DLSS_SDK_ROOT "" CACHE PATH "NVIDIA DLSS SDK root")
set(VEYRA_NVOF_SDK_ROOT "" CACHE PATH "NVIDIA Optical Flow SDK root")
if(NOT VEYRA_NVOF_SDK_ROOT)
  set(VEYRA_NVOF_CANDIDATE "${CMAKE_CURRENT_SOURCE_DIR}/third_party_local/nvidia/Optical_Flow_SDK_5.0.7")
  if(EXISTS "${VEYRA_NVOF_CANDIDATE}/NvOFInterface/nvOpticalFlowCommon.h")
    set(VEYRA_NVOF_SDK_ROOT "${VEYRA_NVOF_CANDIDATE}")
  endif()
endif()
set(VEYRA_RUNTIME_ROOT "" CACHE PATH "Local NVIDIA runtime root")
set(VEYRA_FFMPEG_ROOT "" CACHE PATH "vcpkg-installed x64-windows root with FFmpeg (player deps)")
option(VEYRA_ENABLE_DEINTERLACE "Enable optional LGPL FFmpeg deinterlacing module" ON)
set(VEYRA_CLIP_TOOLS_ROOT "" CACHE PATH "vcpkg-installed x64-windows root with openh264-enabled FFmpeg (clip tooling only)")

option(VEYRA_ENABLE_EXPERIMENTAL_DLSSNR
  "Enable local-only experimental Feature 18 adapter" OFF)
option(VEYRA_ENABLE_REMOTEPLAY "Build PS5 Remote Play with pinned Chiaki source" OFF)
option(VEYRA_ENABLE_MOONLIGHT "Build the Moonlight / Sunshine streaming core (pinned moonlight-common-c)" OFF)
option(VEYRA_ENABLE_XBOX "Build Xbox home streaming (unofficial; libdatachannel from the vcpkg tree)" OFF)
option(VEYRA_ENABLE_DLSS_SR "Enable public DLSS SR backend" OFF)
option(VEYRA_ENABLE_DLSS_FG "Enable public DLSSG backend" OFF)
option(VEYRA_ENABLE_NVOF "Enable NVIDIA Optical Flow guidance" OFF)
option(VEYRA_ENABLE_D3D12_DEBUG "Enable D3D12 debug layer" ON)
set(VEYRA_FIDELITYFX_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/third_party_local/amd/FidelityFX-SDK/sdk" CACHE PATH "Local official FidelityFX SDK 1.1.4")
set(VEYRA_XESS_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/third_party_local/intel/xess-3.0.2" CACHE PATH "Local Intel XeSS SDK 3.0.2")
set(VEYRA_FIDELITYFX2_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/third_party_local/amd/FidelityFX-SDK-2.3.0/Kits/FidelityFX" CACHE PATH "Local AMD FidelityFX SDK 2.3.0 Kits/FidelityFX tree")

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
include(VeyraWarnings)
include(VeyraShaders)

# NVIDIA's static NGX core shim (nvsdk_ngx_s*.lib) is built against the
# static CRT (MT/MTd); match it for the diagnostic tools that link it.
set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")

# Moonlight targets come after the runtime setting: they link into the same
# executables as the rest of the engine, so they must use the static CRT too.
if(VEYRA_ENABLE_MOONLIGHT)
  set(VEYRA_ROOT "${CMAKE_CURRENT_SOURCE_DIR}")
  include(VeyraMoonlight)
  veyra_apply_warnings(veyra_moonlight_protocol)
  add_executable(veyra_moonlight_protocol_tests tests/moonlight/ProtocolTests.cpp)
  target_compile_features(veyra_moonlight_protocol_tests PRIVATE cxx_std_20)
  target_compile_definitions(veyra_moonlight_protocol_tests PRIVATE NOMINMAX WIN32_LEAN_AND_MEAN)
  target_link_libraries(veyra_moonlight_protocol_tests PRIVATE veyra_moonlight_protocol)
  veyra_apply_warnings(veyra_moonlight_protocol_tests)
  # The same fake host as a process, for the end-to-end UI check (scripts/moonlight/ui-demo.py).
  add_executable(veyra_moonlight_mockhost tests/moonlight/MockHostServer.cpp)
  target_compile_features(veyra_moonlight_mockhost PRIVATE cxx_std_20)
  target_compile_definitions(veyra_moonlight_mockhost PRIVATE NOMINMAX WIN32_LEAN_AND_MEAN)
  target_include_directories(veyra_moonlight_mockhost PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/tests/moonlight)
  target_link_libraries(veyra_moonlight_mockhost PRIVATE veyra_moonlight_protocol)
endif()

# ---------------------------------------------------------------------------
# Targets grow phase by phase; only what actually compiles is declared.
# ---------------------------------------------------------------------------
add_library(veyra_base STATIC
  src/base/Log.cpp
  src/base/NgxResult.cpp
  src/base/FileIdentity.cpp
  src/base/RuntimePaths.cpp
  src/base/ThunkHook.cpp
  # .cube parsing, the runtime LUT store and named colour looks: low level, no
  # D3D12, shared by the ingest pipeline and the settings/import paths.
  src/engine/ColorLut.cpp
  src/engine/ColorLookStore.cpp
)
veyra_apply_warnings(veyra_base)
target_compile_options(veyra_base PUBLIC /utf-8)
target_compile_features(veyra_base PUBLIC cxx_std_20)
target_compile_definitions(veyra_base PUBLIC
  UNICODE _UNICODE WIN32_LEAN_AND_MEAN NOMINMAX)
target_include_directories(veyra_base PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_link_libraries(veyra_base PUBLIC bcrypt wintrust crypt32 version)

add_library(veyra_gfx STATIC
  src/gfx/GpuSchedulingPriority.cpp
  src/gfx/D3D12DeviceContext.cpp
  src/gfx/CommandSlotRing.cpp
  src/gfx/PresentSink.cpp
  src/gfx/XessPresenter.cpp
  src/gfx/XessMfgUnlock.cpp
  src/gfx/XessPacing.cpp
  src/gfx/FsrFgPresenter.cpp
  src/gfx/FsrSrBackend.cpp
)
veyra_apply_warnings(veyra_gfx)
target_compile_features(veyra_gfx PUBLIC cxx_std_20)
target_link_libraries(veyra_gfx PUBLIC veyra_base d3d12 dxgi dxguid)
if(EXISTS "${VEYRA_XESS_ROOT}/inc/xess_fg/xefg_swapchain_d3d12.h")
  target_include_directories(veyra_gfx PRIVATE "${VEYRA_XESS_ROOT}/inc")
  target_compile_definitions(veyra_gfx PRIVATE VEYRA_HAS_XESS=1)
endif()
if(EXISTS "${VEYRA_FIDELITYFX2_ROOT}/framegeneration/include/dx12/ffx_api_framegeneration_dx12.h")
  target_include_directories(veyra_gfx PRIVATE
    "${VEYRA_FIDELITYFX2_ROOT}/api/include"
    "${VEYRA_FIDELITYFX2_ROOT}/framegeneration/include"
    "${VEYRA_FIDELITYFX2_ROOT}/upscalers/include")
  target_compile_definitions(veyra_gfx PRIVATE VEYRA_HAS_FSR=1)
endif()
if(VEYRA_ENABLE_D3D12_DEBUG)
  target_compile_definitions(veyra_gfx PUBLIC VEYRA_D3D12_DEBUG=1)
endif()

# ---------------------------------------------------------------------------
# veyra_ngx: NGX core host + local experimental DLSSNR adapter.
# Compiled only with the explicit experimental switch; missing SDK paths are
# a configure-time failure, never a runtime surprise (Playbook 5.1/8.1).
# ---------------------------------------------------------------------------
if(VEYRA_ENABLE_EXPERIMENTAL_DLSSNR)
  if(NOT VEYRA_DLSS_SDK_ROOT OR NOT EXISTS "${VEYRA_DLSS_SDK_ROOT}/include/nvsdk_ngx.h")
    message(FATAL_ERROR "VEYRA_ENABLE_EXPERIMENTAL_DLSSNR requires VEYRA_DLSS_SDK_ROOT pointing at NVIDIA DLSS SDK 310.7 (include/nvsdk_ngx.h missing)")
  endif()
add_library(veyra_ngx STATIC
  src/ngx/NgxCoreHost.cpp
  src/ngx/NgxCoreCache.cpp
  src/ngx/DlssNrRuntimeAdapter.cpp
  src/ngx/NvapiLifetime.cpp
  src/ngx/DlssSrBackend.cpp
    src/ngx/VideoSrBackend.cpp
    src/ngx/TrueHdrBackend.cpp
  src/ngx/DlssFgBackend.cpp
  src/ngx/FgCompatibilitySession.cpp
  src/ngx/compat/hde/hde64.c
  src/ngx/AdaMfgUnlock.cpp
  src/ngx/AmpereMfgUnlock.cpp
  src/ngx/NvapiArchSpoof.cpp
  src/ngx/DlssgTransfusion.cpp
)
  set_source_files_properties(src/ngx/compat/hde/hde64.c PROPERTIES LANGUAGE CXX)
  veyra_apply_warnings(veyra_ngx)
  target_compile_features(veyra_ngx PUBLIC cxx_std_20)
  target_link_libraries(veyra_ngx PUBLIC veyra_base veyra_gfx d3d11)
  target_include_directories(veyra_ngx PUBLIC
    "${VEYRA_DLSS_SDK_ROOT}/include")
  # NVIDIA ships the static core shim as MT-Release; the _dbg variants match
  # the MDd debug runtime. Pick per configuration to avoid LNK2038.
  target_link_libraries(veyra_ngx PRIVATE
    "$<IF:$<CONFIG:Debug>,${VEYRA_DLSS_SDK_ROOT}/lib/Windows_x86_64/x64/nvsdk_ngx_s_dbg.lib,${VEYRA_DLSS_SDK_ROOT}/lib/Windows_x86_64/x64/nvsdk_ngx_s.lib>")
  target_compile_definitions(veyra_ngx PUBLIC
    VEYRA_EXPERIMENTAL_LOCAL_DLSSNR=1 VEYRA_HAS_NGX_CORE_CACHE=1 VEYRA_HAS_PAUSED_NR_RESIDUAL_REUSE=1)

  # Diagnostic: exercises the Ada multi-frame unlock against the local DLSS-G
  # runtime image without involving NGX (works on any NVIDIA adapter).
  add_executable(veyra_dlssg_unlock_probe tools/dlssg_unlock_probe/main.cpp)
  target_compile_features(veyra_dlssg_unlock_probe PRIVATE cxx_std_20)
  target_compile_options(veyra_dlssg_unlock_probe PRIVATE /utf-8 /WX-)
  target_compile_definitions(veyra_dlssg_unlock_probe PRIVATE NOMINMAX WIN32_LEAN_AND_MEAN UNICODE _UNICODE)
  target_link_libraries(veyra_dlssg_unlock_probe PRIVATE veyra_ngx)

  # Diagnostic: exercises the RTX 30 (sm_86) Ampere unlock against the local
  # DLSS-G runtime image without involving NGX (works on any NVIDIA adapter).
  add_executable(veyra_dlssg_ampere_probe tools/dlssg_ampere_probe/main.cpp)
  target_compile_features(veyra_dlssg_ampere_probe PRIVATE cxx_std_20)
  target_compile_options(veyra_dlssg_ampere_probe PRIVATE /utf-8 /WX-)
  target_compile_definitions(veyra_dlssg_ampere_probe PRIVATE NOMINMAX WIN32_LEAN_AND_MEAN UNICODE _UNICODE)
  target_link_libraries(veyra_dlssg_ampere_probe PRIVATE veyra_ngx)
endif()

add_executable(veyra_runtime_probe
  tools/runtime_probe/main.cpp
)

# Dolby/DTS endpoint passthrough capability probe (diagnostic, never shipped).
add_executable(veyra_bitstream_probe tools/bitstream_audio_probe/main.cpp)
target_compile_features(veyra_bitstream_probe PRIVATE cxx_std_20)
target_compile_options(veyra_bitstream_probe PRIVATE /utf-8 /WX-)
target_compile_definitions(veyra_bitstream_probe PRIVATE NOMINMAX WIN32_LEAN_AND_MEAN UNICODE _UNICODE)
target_link_libraries(veyra_bitstream_probe PRIVATE ole32)

# Isolated descriptor/Present diagnosis probe (user directive 2026-09-04 s3).
# No NGX/FFmpeg/NVOF/WASAPI. Uses PresentBlit shaders for cases F/G.
add_executable(veyra_descriptor_present_probe
  tools/descriptor_present_probe/main.cpp
)
veyra_apply_warnings(veyra_descriptor_present_probe)
target_compile_features(veyra_descriptor_present_probe PRIVATE cxx_std_20)
target_compile_definitions(veyra_descriptor_present_probe PRIVATE
  UNICODE _UNICODE WIN32_LEAN_AND_MEAN NOMINMAX
  VEYRA_SHADER_DIR="${CMAKE_BINARY_DIR}/shaders")
target_link_libraries(veyra_descriptor_present_probe PRIVATE d3d12 dxgi)
add_dependencies(veyra_descriptor_present_probe veyra_shader_present_blit)
veyra_apply_warnings(veyra_runtime_probe)
target_compile_features(veyra_runtime_probe PRIVATE cxx_std_20)
target_compile_definitions(veyra_runtime_probe PRIVATE
  UNICODE _UNICODE WIN32_LEAN_AND_MEAN NOMINMAX)
target_link_libraries(veyra_runtime_probe PRIVATE veyra_gfx)

veyra_add_compute_shader(veyra_shader_parity_encode ParityEncode)
veyra_add_compute_shader(veyra_shader_parity_decode ParityDecode)
veyra_add_compute_shader(veyra_shader_rdna3_nr_decode Rdna3NrDecode)
veyra_add_compute_shader(veyra_shader_hdr_video_sr HdrVideoSrRestore)
veyra_add_compute_shader(veyra_shader_sr_resolve SrResolve)
veyra_add_compute_shader(veyra_shader_hdr_amd_nr_encode HdrAmdNrEncode)
veyra_add_compute_shader(veyra_shader_hdr_amd_nr_restore HdrAmdNrRestore)
if(VEYRA_ENABLE_EXPERIMENTAL_DLSSNR)
  veyra_add_compute_shader(veyra_shader_test_pattern GenerateTestPattern)
  add_executable(veyra_nr_ampere_tests tests/integration/NrAmpereTests.cpp)
  target_compile_features(veyra_nr_ampere_tests PRIVATE cxx_std_20)
  target_compile_definitions(veyra_nr_ampere_tests PRIVATE UNICODE _UNICODE WIN32_LEAN_AND_MEAN NOMINMAX)
  target_link_libraries(veyra_nr_ampere_tests PRIVATE veyra_gfx veyra_ngx)
  add_executable(veyra_nvapi_lifetime_tests tests/integration/NvapiLifetimeTests.cpp)
  target_compile_features(veyra_nvapi_lifetime_tests PRIVATE cxx_std_20)
  target_compile_definitions(veyra_nvapi_lifetime_tests PRIVATE UNICODE _UNICODE WIN32_LEAN_AND_MEAN NOMINMAX)
  target_link_libraries(veyra_nvapi_lifetime_tests PRIVATE veyra_ngx)
  add_executable(veyra_nr_harness
    tools/nr_harness/main.cpp
    tools/nr_harness/frame_loop.cpp
    tools/nr_harness/harness_util.cpp
    tools/nr_harness/parity_compare.cpp
    tools/nr_harness/sr_test.cpp
  )
  veyra_apply_warnings(veyra_nr_harness)
  target_compile_features(veyra_nr_harness PRIVATE cxx_std_20)
  target_compile_definitions(veyra_nr_harness PRIVATE
    UNICODE _UNICODE WIN32_LEAN_AND_MEAN NOMINMAX
    VEYRA_SHADER_DIR="${CMAKE_BINARY_DIR}/shaders")
  target_link_libraries(veyra_nr_harness PRIVATE veyra_gfx veyra_ngx veyra_parity)
  add_dependencies(veyra_nr_harness veyra_shader_test_pattern
    veyra_shader_parity_encode veyra_shader_parity_decode)

  # NR stacking probe: several Feature-18 handles on one snippet session.
  add_executable(veyra_nr_probe
    tools/nr_probe/main.cpp
    tools/nr_harness/harness_util.cpp
  )
  veyra_apply_warnings(veyra_nr_probe)
  target_compile_features(veyra_nr_probe PRIVATE cxx_std_20)
  target_compile_definitions(veyra_nr_probe PRIVATE
    UNICODE _UNICODE WIN32_LEAN_AND_MEAN NOMINMAX
    VEYRA_SHADER_DIR="${CMAKE_BINARY_DIR}/shaders")
  target_link_libraries(veyra_nr_probe PRIVATE veyra_gfx veyra_ngx)

  # Phase 6: DLSSG truth harness + WASAPI audio probe.
  add_executable(veyra_fg_harness
    tools/fg_harness/main.cpp
    tools/fg_harness/fg_test.cpp
    tools/fg_harness/audio_test.cpp
    tools/nr_harness/harness_util.cpp
  )
  veyra_apply_warnings(veyra_fg_harness)
  target_compile_features(veyra_fg_harness PRIVATE cxx_std_20)
  target_compile_definitions(veyra_fg_harness PRIVATE
    UNICODE _UNICODE WIN32_LEAN_AND_MEAN NOMINMAX)
  target_link_libraries(veyra_fg_harness PRIVATE veyra_gfx veyra_ngx ole32 mmdevapi avrt)
endif()

# YUV→RGB shader is shared between the media pipeline and the harness.
veyra_add_compute_shader(veyra_shader_yuv_to_rgb YuvToLinearRgb)
veyra_add_compute_shader(veyra_shader_rgb_to_linear RgbToLinear)
veyra_add_compute_shader(veyra_shader_color_grade ColorGradePass)
# 纹理 / 清晰度 / 去朦胧: block statistics, blur, apply (ColorDetailPass).
veyra_add_compute_shader(veyra_shader_color_detail_reduce ColorDetailReduce)
veyra_add_compute_shader(veyra_shader_color_detail_blur ColorDetailBlur)
veyra_add_compute_shader(veyra_shader_color_detail_apply ColorDetailApply)
veyra_add_compute_shader(veyra_shader_yuy2_to_linear Yuy2ToLinear)
veyra_add_compute_shader(veyra_shader_packed_capture PackedCaptureToLinear)
add_dependencies(veyra_shader_rgb_to_linear veyra_shader_yuy2_to_linear)
# ScaleBlit: working frame -> swapchain backbuffer (Phase 6 present path).
veyra_add_compute_shader(veyra_shader_scale_blit ScaleBlit)
# Nv12Upload: byte buffer -> luma/chroma planes (copy-free upload path).
veyra_add_compute_shader(veyra_shader_nv12_upload Nv12Upload)
# PresentBlit: fullscreen-triangle pixel blit onto flip-model back buffers.
veyra_add_graphics_shader_pair(veyra_shader_present_blit PresentBlit)
veyra_add_compute_shader(veyra_shader_present_motion PresentMotion)
veyra_add_compute_shader(veyra_shader_hdr_coverage HdrCurveCoverage)
# NvofDensify: SHORT2 S10.5 raw flow -> workingExtent float2 + confidence.
veyra_add_compute_shader(veyra_shader_nvof_densify NvofDensify)
veyra_add_compute_shader(veyra_shader_nr_downsample NrDownsample)
veyra_add_compute_shader(veyra_shader_nr_residual NrResidualComposite)
veyra_add_compute_shader(veyra_shader_nr_temporal NrTemporal)
# Stage-5 output stabiliser (anti-flicker, default off).
veyra_add_compute_shader(veyra_shader_nr_hold NrHold)
# NR inference reuse (realtime preview only, default off).
veyra_add_compute_shader(veyra_shader_nr_reuse_compose NrReuseCompose)
veyra_add_compute_shader(veyra_shader_nr_reuse_warp NrReuseWarp)
veyra_add_compute_shader(veyra_shader_flow_adapt FlowAdapt)
veyra_add_compute_shader(veyra_shader_flow_refine FlowRefine)
veyra_add_compute_shader(veyra_shader_flow_fill FlowFill)
veyra_add_compute_shader(veyra_shader_flow_claim FlowClaim)
# VfgShotChange: per-pair shot-change test for VFG (replaces the SDK's automatic one).
veyra_add_compute_shader(veyra_shader_vfg_shot_change VfgShotChange)
veyra_add_compute_shader(veyra_shader_rgb_nv12 RgbToNv12)

# ---------------------------------------------------------------------------
# veyra_parity: RenoDX-equivalent codec reference (CPU golden + shaders later).
# The CPU reference has no D3D12 dependency, so it builds unconditionally.
# ---------------------------------------------------------------------------
add_library(veyra_parity STATIC
  src/parity/RenoDxParityCodec.cpp
)
veyra_apply_warnings(veyra_parity)
target_compile_features(veyra_parity PUBLIC cxx_std_20)
target_link_libraries(veyra_parity PUBLIC veyra_base)

add_executable(veyra_parity_tests
  tests/unit/ParityCpuReference.cpp
)
veyra_apply_warnings(veyra_parity_tests)
target_compile_features(veyra_parity_tests PRIVATE cxx_std_20)
target_compile_definitions(veyra_parity_tests PRIVATE
  UNICODE _UNICODE WIN32_LEAN_AND_MEAN NOMINMAX)
target_link_libraries(veyra_parity_tests PRIVATE veyra_parity)

add_executable(veyra_unified_tests
  tests/unit/UnifiedContractTests.cpp
  src/core/EnhanceGraph.cpp
)
veyra_apply_warnings(veyra_unified_tests)
target_compile_features(veyra_unified_tests PRIVATE cxx_std_20)
target_compile_definitions(veyra_unified_tests PRIVATE
  UNICODE _UNICODE WIN32_LEAN_AND_MEAN NOMINMAX)
target_include_directories(veyra_unified_tests PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_link_libraries(veyra_unified_tests PRIVATE d3d12 veyra_gfx veyra_ngx)

# Guidance product library (Playbook R3/R4): providers produce the unified
# GuidanceFrame. First real member: ZeroGuidanceProvider (honest fallback).
# NvofGuidanceProvider moves in from player_probe during R3.2.
add_library(veyra_guidance STATIC
  src/guidance/ZeroGuidanceProvider.cpp
)
veyra_apply_warnings(veyra_guidance)
target_compile_options(veyra_guidance PRIVATE /WX-)
target_compile_features(veyra_guidance PRIVATE cxx_std_20)
target_compile_definitions(veyra_guidance PRIVATE
  UNICODE _UNICODE WIN32_LEAN_AND_MEAN NOMINMAX)
target_include_directories(veyra_guidance PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_link_libraries(veyra_guidance PUBLIC veyra_pipeline veyra_gfx veyra_base d3d12 dxgi dxguid)

add_executable(veyra_guidance_tests
  tests/inte

[… 126498 バイトのうち先頭 20000 バイトだけ保存した]
