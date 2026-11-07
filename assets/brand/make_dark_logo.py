"""GDG Kastamonu logosunu (beyaz zeminli JPG) koyu video arka planı için şeffaf PNG'ye çevirir.

- Beyaz zemin "color to alpha" ile şeffaflaşır (JPEG gürültüsü eşiklenir).
- Sağdaki koyu gri yazı ("Google Developer Group") beyaza çevrilir; mavi alt yazı ve renkli parantezler korunur.
- Parantezlerin siyah konturu koyu zeminde gereksiz olduğu için kaldırılır.
Ayrıca açık (krem) video zemini için renkleri değiştirilmemiş gdg_logo_light.png üretilir.
Kullanım: python assets/brand/make_dark_logo.py
"""
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).parent

im = np.asarray(Image.open(HERE / "gdg_logo_original.jpg").convert("RGB")).astype(np.float32)
ys, xs = np.where(im.min(axis=2) < 200)
im = im[ys.min() - 4:ys.max() + 4, xs.min() - 4:xs.max() + 4]

# Color to alpha (beyaza göre): her pikselin beyazdan ne kadar uzak olduğu
alpha = np.clip((255 - im.min(axis=2)) / 255, 0, 1)
alpha = np.clip((alpha - 0.10) / 0.75, 0, 1)  # JPEG beneklerini sil, kenarları keskinleştir
a = np.maximum(alpha, 1e-3)[..., None]
color = np.clip((im - 255 * (1 - a)) / a, 0, 255)

light = np.dstack([color, alpha * 255]).astype(np.uint8)
light_img = Image.fromarray(light, "RGBA")
light_img.resize((light_img.width * 3, light_img.height * 3), Image.LANCZOS).save(HERE / "gdg_logo_light.png")

mx, mn = color.max(axis=2), color.min(axis=2)
neutral_dark = ((mx - mn) < 40) & (mx < 140)
# Parantezler sol tarafta; yazı sağda. Parantez ile yazı arasındaki boş sütunu bul
cols = (alpha > 0.5).any(axis=0)
gap = next(x for x in range(int(len(cols) * 0.15), len(cols)) if not cols[x])
text = np.zeros_like(neutral_dark)
text[:, gap:] = True

color[neutral_dark & text] = 255           # koyu yazı -> beyaz
color[~neutral_dark & text] = (110, 160, 255)  # mavi alt yazı koyu zeminde okunsun diye açılır
alpha[neutral_dark & ~text] = 0            # parantez konturu -> şeffaf

rgba = np.dstack([color, alpha * 255]).astype(np.uint8)
img = Image.fromarray(rgba, "RGBA")
img = img.resize((img.width * 3, img.height * 3), Image.LANCZOS)
img.save(HERE / "gdg_logo.png")
print("gdg_logo.png", img.size, "ayraç sütunu:", gap)
