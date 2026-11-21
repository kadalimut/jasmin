#!/usr/bin/env python3
"""Draw the 21 November 2026 world-news image.

Output is a 1024x1024 PNG, under 1 MiB, deterministic.
Run: python3 tools/draw_image.py
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1024, 1024
BG = (253, 248, 238)
NAVY = (18, 38, 66)
GOLD = (198, 142, 32)
WHITE = (255, 255, 255)
DARK = (28, 28, 28)
GREY = (90, 90, 90)
PANEL_BG = (255, 255, 255)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=fnt) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_panel(draw, x, y, w, h, color, kicker, title, lines, icon):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=PANEL_BG, outline=(210, 205, 190), width=2)
    draw.rounded_rectangle([x, y, x + w, y + 8], radius=4, fill=color)
    draw.ellipse([x + 16, y + 22, x + 64, y + 70], fill=color)
    f_icon = font(FONT_BOLD, 26)
    tw = draw.textlength(icon, font=f_icon)
    draw.text((x + 40 - tw / 2, y + 28), icon, font=f_icon, fill=WHITE)
    f_kick = font(FONT_BOLD, 15)
    draw.text((x + 78, y + 26), kicker, font=f_kick, fill=color)
    f_title = font(FONT_BOLD, 23)
    ty = y + 84
    for line in wrap(draw, title, f_title, w - 32):
        draw.text((x + 16, ty), line, font=f_title, fill=DARK)
        ty += 28
    f_body = font(FONT_REG, 17)
    by = ty + 8
    for line in lines:
        for sub in wrap(draw, line, f_body, w - 32):
            draw.text((x + 16, by), sub, font=f_body, fill=(60, 60, 60))
            by += 23


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 148], fill=NAVY)
    draw.rectangle([0, 148, W, 156], fill=GOLD)
    f_small = font(FONT_BOLD, 18)
    draw.text((32, 18), "THE WORLD IN ONE DAY", font=f_small, fill=(220, 180, 80))
    f_date = font(FONT_SERIF, 44)
    draw.text((30, 46), "SATURDAY, 21 NOVEMBER 2026", font=f_date, fill=WHITE)
    f_sub = font(FONT_REG, 18)
    draw.text((32, 108), "Six stories from one day  •  21 Nov 2026", font=f_sub, fill=(200, 210, 225))
    panels = [
        ("EUROPE  •  WAR", "RUSSIA HITS POLAND", ["Missiles land in Poland.", "Tusk: deliberate", "provocation. NATO on alert."], "!", (178, 34, 34)),
        ("UKRAINE", "UKRAINE UNDER FIRE", ["110+ missiles, 400 drones.", "8 killed. Kyiv bridges hit."], "*", (200, 90, 20)),
        ("BRITAIN  •  EUROPE", "UK-EU LANDMARK DEAL", ["Brexit reset: food trade,", "youth visas for 100,000."], "+", (20, 90, 160)),
        ("DIPLOMACY", "TRUMP-XI-PUTIN SUMMIT", ["Shenzhen peace declaration:", "no nuclear war, ever."], "3", (90, 60, 140)),
        ("JUSTICE", "ICJ: MYANMAR GUILTY", ["First state found guilty", "of genocide, 9-6. Myanmar", "rejects the ruling."], "§", (120, 40, 90)),
        ("EUROPE  •  AID", "EU GIVES €1BN TO UKRAINE", ["Drones and air defence,", "delivered by end of 2027."], "€", (0, 120, 80)),
    ]
    x0, y0 = 24, 176
    pw, ph = 476, 258
    gx, gy = 24, 20
    for i, (kicker, title, lines, icon, color) in enumerate(panels):
        col = i % 2
        row = i // 2
        x = x0 + col * (pw + gx)
        y = y0 + row * (ph + gy)
        draw_panel(draw, x, y, pw, ph, color, kicker, title, lines, icon)
    draw.rectangle([0, 976, W, H], fill=NAVY)
    f_foot = font(FONT_BOLD, 16)
    draw.text((32, 986), "21 NOV 2026  •  6 STORIES  •  NEWS-IMAGE-20261121", font=f_foot, fill=WHITE)
    out = os.path.join(os.path.dirname(__file__), "..", "entry.png")
    out = os.path.normpath(out)
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
