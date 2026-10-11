"""リポジトリごとの OGP 画像（1200×630 の PNG）を作る（0039）。

入力が同じなら出力も同じ（フォントは同梱、PNG に時刻などは入れない）。
X・Discord・Slack に URL を貼ったときのカードに出る。
"""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONTS = Path(__file__).parent / "fonts"
STATIC = Path(__file__).parent / "static"

W, H = 1200, 630
MARGIN = 64
PAPER = (230, 233, 236)      # ライトの紙の色（style.css の --paper）
INK = (26, 28, 31)
MUTED = (96, 102, 110)
ACCENT = (179, 38, 30)       # 差し色（#b3261e）
EDGE = (155, 162, 170)       # 紙面の枠（--edge）

# 行の頭に来てはいけない文字（行末に付ける）
NO_LINE_START = set("、。，．）」』】〉》・ー！？!?,.)]}:;")
# 英数字のひとかたまり（単語の途中で折らない）
WORD = re.compile(r"[A-Za-z0-9_.\-/+#@:]+")


@lru_cache(maxsize=None)
def _gothic(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / "BIZUDPGothic-Bold.ttf"), size)


@lru_cache(maxsize=None)
def _serif(size: int, weight: str = "Bold") -> ImageFont.FreeTypeFont:
    font = ImageFont.truetype(str(FONTS / "Gelasio-Variable.ttf"), size)
    font.set_variation_by_name(weight)
    return font


@lru_cache(maxsize=1)
def _logo() -> Image.Image:
    logo = Image.open(STATIC / "logo_light.png").convert("RGBA")
    width = 380
    return logo.resize((width, round(logo.height * width / logo.width)), Image.LANCZOS)


def _tokens(text: str) -> list[str]:
    """折り返しの単位：英数字のかたまりは1つ、それ以外は1文字ずつ。"""
    out, i = [], 0
    for m in WORD.finditer(text):
        out.extend(text[i:m.start()])
        out.append(m.group())
        i = m.end()
    out.extend(text[i:])
    return out


def wrap(text: str, font: ImageFont.FreeTypeFont, width: int, max_lines: int) -> list[str]:
    """日本語の文を幅に収まるよう折り返す。入りきらなければ最後の行を「…」で終える。"""
    lines: list[str] = []
    line = ""
    tokens = _tokens(text)
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if font.getlength(line + tok) <= width or not line:
            line += tok
            i += 1
            continue
        if tok in NO_LINE_START:  # 句読点は前の行の末に付ける
            line += tok
            i += 1
        lines.append(line.rstrip())
        line = ""
        if len(lines) == max_lines:
            break
    if line and len(lines) < max_lines:
        lines.append(line.rstrip())
    elif i < len(tokens) and lines:
        last = lines[-1]
        while last and font.getlength(last + "…") > width:
            last = last[:-1]
        lines[-1] = last + "…"
    return lines


def _fit_serif(text: str, width: int, start: int, smallest: int) -> ImageFont.FreeTypeFont:
    """リポジトリ名が1行に収まる大きさを探す。"""
    size = start
    while size > smallest and _serif(size).getlength(text) > width:
        size -= 4
    return _serif(size)


def render(repo: str, what: str, language: str | None = None, site: str = "") -> Image.Image:
    owner, _, name = repo.partition("/")
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # 紙面の二重の枠（サイトと同じ）
    d.rectangle([14, 14, W - 15, H - 15], outline=EDGE, width=3)
    d.rectangle([22, 22, W - 23, H - 23], outline=EDGE, width=1)

    # 題字と、表罫（太い線と細い線）
    logo = _logo()
    img.paste(logo, (MARGIN, 52), logo)
    kicker = _gothic(26)
    d.text((W - MARGIN, 96), "リポジトリ解説", font=kicker, fill=ACCENT, anchor="rs")
    y = 52 + logo.height + 18
    d.rectangle([MARGIN, y, W - MARGIN, y + 5], fill=INK)
    d.rectangle([MARGIN, y + 11, W - MARGIN, y + 12], fill=INK)

    # アカウント名と、リポジトリ名
    y += 40
    d.text((MARGIN, y), f"{owner}/", font=_serif(34, "Regular"), fill=MUTED)
    if language:
        d.text((W - MARGIN, y + 4), language, font=_gothic(28), fill=MUTED, anchor="ra")
    y += 46
    title = _fit_serif(name, W - 2 * MARGIN, 96, 48)
    d.text((MARGIN, y), name, font=title, fill=INK)
    y += title.size + 40

    # 何をするものか（2行まで）
    body = _gothic(44)
    for line in wrap(what, body, W - 2 * MARGIN, 2):
        d.text((MARGIN, y), line, font=body, fill=INK)
        y += 62

    # 下の欄：標語とドメイン、言語
    foot_y = H - 92
    d.rectangle([MARGIN, foot_y, W - MARGIN, foot_y + 1], fill=INK)
    small = _gothic(24)
    d.text((MARGIN, foot_y + 22), "GitHub トレンドの人気リポジトリを、毎朝日本語で", font=small, fill=MUTED)
    if site:
        d.text((W - MARGIN, foot_y + 22), site, font=small, fill=MUTED, anchor="ra")
    return img


def write(path: Path, repo: str, what: str, language: str | None = None, site: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    render(repo, what, language, site).save(path, format="PNG", optimize=True)
