"""Generate the Chinese demo artwork for the dsh-quick-reload README.

These are illustrative diagrams (示意图), not real screenshots: the two panels
show the cached slash menu before and after an F5 reload. The skill names and
their alphabetical order are taken from a real session.
"""

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "docs")
os.makedirs(OUT, exist_ok=True)

FONTS = r"C:\Windows\Fonts"
REG = os.path.join(FONTS, "msyh.ttc")      # Microsoft YaHei
BOLD = os.path.join(FONTS, "msyhbd.ttc")


def font(path, size):
    return ImageFont.truetype(path, size, index=0)


# Palette (GitHub-like, matching the plugin icon accent).
BG = (240, 242, 245)
PANEL = (255, 255, 255)
BORDER = (208, 215, 222)
TEXT = (31, 35, 40)
MUTED = (101, 109, 118)
FAINT = (139, 148, 158)
ACCENT = (9, 105, 218)
ACCENT_BG = (221, 244, 255)
ACCENT_BR = (84, 174, 255)
GOOD = (26, 127, 55)
GOOD_BG = (218, 251, 225)
BAD = (207, 34, 46)


def rounded(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(draw, xy, s, f, fill, anchor="la"):
    draw.text(xy, s, font=f, fill=fill, anchor=anchor)


def keycap(img, cx, cy, w=132, h=132, label="F5"):
    """Draw an F5 keycap centred on (cx, cy)."""
    d = ImageDraw.Draw(img)
    x0, y0 = cx - w // 2, cy - h // 2
    # base plate (gives the cap a physical bottom edge)
    rounded(d, (x0, y0 + 10, x0 + w, y0 + h + 10), 24, fill=(180, 188, 198))
    rounded(d, (x0, y0, x0 + w, y0 + h), 24, fill=(255, 255, 255),
            outline=(160, 170, 182), width=3)
    text(d, (cx, cy + 4), label, font(BOLD, 44), ACCENT, anchor="mm")


def check(draw, x, y, color):
    draw.line([(x, y + 5), (x + 4, y + 9), (x + 12, y - 1)], fill=color, width=3, joint="curve")


def cross(draw, x, y, color):
    draw.line([(x, y), (x + 11, y + 11)], fill=color, width=3)
    draw.line([(x + 11, y), (x, y + 11)], fill=color, width=3)


def panel(img, x, y, w, h, title, items, highlight=None, status=None, status_ok=False):
    d = ImageDraw.Draw(img)
    rounded(d, (x + 3, y + 5, x + w + 3, y + h + 5), 16, fill=(226, 229, 234))
    rounded(d, (x, y, x + w, y + h), 16, fill=PANEL, outline=BORDER, width=2)

    text(d, (x + 26, y + 24), title, font(BOLD, 22), TEXT)

    # mock slash-menu input line
    ib = (x + 26, y + 62, x + w - 26, y + 110)
    rounded(d, ib, 10, fill=(246, 248, 250), outline=BORDER, width=2)
    text(d, (x + 44, y + 86), "/", font(REG, 24), ACCENT, anchor="lm")
    text(d, (x + 66, y + 86), "输入技能名筛选…", font(REG, 17), FAINT, anchor="lm")

    text(d, (x + 26, y + 126), "技能", font(REG, 15), FAINT)

    # 44px rows on a 46px pitch so a five-item list still clears the status line.
    iy = y + 148
    for name in items:
        hit = highlight is not None and name == highlight
        box = (x + 22, iy, x + w - 22, iy + 40)
        if hit:
            rounded(d, box, 8, fill=ACCENT_BG, outline=ACCENT_BR, width=2)
        text(d, (x + 40, iy + 20), name, font(REG, 18),
             ACCENT if hit else TEXT, anchor="lm")
        if hit:
            text(d, (x + w - 40, iy + 20), "新", font(BOLD, 14), ACCENT, anchor="rm")
        iy += 46

    if status:
        sy = y + h - 36
        if status_ok:
            check(d, x + 28, sy - 6, GOOD)
        else:
            cross(d, x + 28, sy - 6, BAD)
        text(d, (x + 50, sy), status, font(REG, 17), GOOD if status_ok else BAD, anchor="lm")


# ---------------------------------------------------------------- demo.png
W, H = 1280, 660
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

text(d, (W // 2, 46), "装完 skill，斜杠菜单里却没有？", font(BOLD, 32), TEXT, anchor="mm")
text(d, (W // 2, 92), "按一次 F5 重载界面，无需重启客户端", font(REG, 19), MUTED, anchor="mm")

BEFORE = ["diagnose-windows-sandbox-acl", "office-docx", "office-pptx", "office-xlsx"]
AFTER = BEFORE + ["qa-req2testcase-generator"]

panel(img, 46, 132, 470, 440, "按 F5 之前", BEFORE,
      status="新装的 skill 不出现")
panel(img, 764, 132, 470, 440, "按 F5 之后", AFTER,
      highlight="qa-req2testcase-generator",
      status="新装的 skill 立即出现", status_ok=True)

keycap(img, W // 2, 330)
text(d, (W // 2, 424), "按 F5", font(BOLD, 20), ACCENT, anchor="mm")

text(d, (W // 2, 612), "示意图：演示菜单缓存的刷新效果，非真实截图",
     font(REG, 15), FAINT, anchor="mm")

img.save(os.path.join(OUT, "demo.png"), "PNG", optimize=True)

# ---------------------------------------------------------------- f5.png
W2, H2 = 520, 220
img2 = Image.new("RGB", (W2, H2), BG)
keycap(img2, W2 // 2, 92, w=112, h=112)
d2 = ImageDraw.Draw(img2)
text(d2, (W2 // 2, 178), "按 F5 刷新界面", font(BOLD, 21), TEXT, anchor="mm")
img2.save(os.path.join(OUT, "f5.png"), "PNG", optimize=True)

for name in ("demo.png", "f5.png"):
    p = os.path.join(OUT, name)
    with Image.open(p) as im:
        print(f"{name}: {im.size[0]}x{im.size[1]}, {os.path.getsize(p) / 1024:.1f} KB")
