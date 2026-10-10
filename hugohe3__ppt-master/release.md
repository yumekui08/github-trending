tag: v6.7.0
name: v6.7.0
published_at: 2026-10-08T02:01:38Z
prerelease: False

Minor release: a browser review page for the design spec, Google's new Nano Banana 2.1 as the default Google image model, and fixes for content that source conversion and PPTX/SVG text round-trips used to lose without a warning.

## Image generation

- **Google image generation now defaults to Nano Banana 2.1** (`gemini-nano-banana-2.1`, GA on 2026-10-06), on the Gemini, OpenRouter (`google/gemini-nano-banana-2.1`) and fal (`google/nano-banana-2.1`) backends. Google has deprecated `gemini-3.1-flash-image`, but has not announced a shutdown date. Nano Banana 2.1 does not offer `512px`, so all three backends now reject `512px` for it before sending a request. The wide ratios `1:4 4:1 1:8 8:1` still work (35508e34).
  - **If your `.env` pins `GEMINI_MODEL=gemini-3.1-flash-image`** (or the OpenRouter/fal equivalent), that setting still wins over the new default. Update or remove the line to switch.
  - Removed the IDs `gemini-3.1-flash-image-preview` and `gemini-2.5-flash-image-preview`; Google has shut both models down.
- **OpenAI**: `OPENAI_BACKGROUND=transparent` is now accepted for GPT Image models, including `gpt-image-2` (in preview at OpenAI), and is refused only together with JPEG output. `gpt-image-2.5-sunburst` / `gpt-image-2.5-flare` and their snapshots accept `OPENAI_QUALITY=xhigh|max`. `gpt-image-1-mini` accepts input fidelity `low` only. The default stays `gpt-image-2` (3f98568c).
- **Backend fixes**:
  - Qwen 2K `2:3` / `3:2` used to produce 3:4 / 4:3 images.
  - A Volcengine Ark base URL ending in `/api/v3` no longer gets `/api/v1` appended.
  - Replicate now rejects `21:9`, which `flux-1.1-pro` does not offer, before sending the request (06d8f0a1).
- `image_search` halves originals above Pillow's decompression-warning size (481e057e). `slice_images` handles three more cases (964d9209, fd20665d, adbfdf48):
  - a ground that is uneven but key-coloured;
  - edges and shadows blended with the key colour;
  - despill on a ground measured close to the key colour.

## Design spec review

- **New browser review page for `design_spec.md`**: one page per section, Part and slide. You can edit one block's Markdown directly. The edit is applied as an exact byte-range replacement with a hash precondition, and its schema is checked before it is written. You can also leave per-block or global comments, which go in a separate sidecar file and never into the spec. `check_spec_annotations.py` hands both kinds of feedback to the agent (aec32024, 61ad7aec).
- With `refine_spec` on, a run that confirmed on the page now also reviews the spec on the page; runs confirmed in chat keep reviewing in chat. Approval still happens in chat. Resume returns to Refine Spec if the spec changed after the lock (866efd84).

## Source conversion

- **DOCX, PPTX, Excel and web converters no longer drop content without a warning.** Affected content included nested tables, content controls, endnotes and links inside tables, OMML separators, PPTX field text and numbering continuation, Excel hidden sheets, merged cells and number formats, and more (13ac724c, 2d72da61).
- `pdf_to_md` keeps body text that repeats a running header or footer, and keeps numeric or labelled paragraphs that sit between tables sharing a header (51c2979a, 4eb7b3d6). Typst text survives when pandoc cannot evaluate it (176235a3).

## PPTX ↔ SVG text

- Text baselines now come from one shared font-metric model in both directions, replacing fixed font-size estimates (3d1b7dc6, #301).
- Imported text that overflows its frame keeps every line, following DrawingML's default overflow, and stays vertically anchored. Explicit clip and ellipsis are still honoured (c9a82582, d5424756).

## UI and tooling

- Spec review, confirmation and live preview UIs:
  - all detect and store the UI language the same way;
  - switching language keeps typed annotations;
  - zh-TW uses full-width separators.
  Thanks to @kevindesuyo (#305, #306, #307).
- Detached servers keep ANSI colour codes out of their logs (1d76e326). The bundled comparison gallery and logos are smaller (6a9ee2aa).

## Sponsors

- Added the international Kimi Code link next to the domestic one (#296), and removed a sponsor whose sponsorship term ended (680de11f).
