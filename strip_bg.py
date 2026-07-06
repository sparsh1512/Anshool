import numpy as np
from PIL import Image
import sys, os

def remove_white_bg(path, out_path, threshold=246, feather=30):
    img = Image.open(path).convert("RGBA")
    arr = np.array(img).astype(np.float32)
    rgb = arr[:, :, :3]
    min_val = rgb.min(axis=2)
    alpha = np.clip((threshold - min_val) / feather, 0, 1) * 255
    arr[:, :, 3] = np.minimum(arr[:, :, 3], alpha)
    out = Image.fromarray(arr.astype(np.uint8), "RGBA")
    out.save(out_path)
    # trim fully-transparent border to tighten bounding box
    bbox = out.getbbox()
    if bbox:
        out.crop(bbox).save(out_path)
    print(f"{os.path.basename(path)} -> {os.path.basename(out_path)}  size={out.size}")

jobs = [
    ("1748425751803.jpg", "deccanai_t.png"),
    ("Maruti_Suzuki_logo.svg.png", "maruti_t.png"),
    ("download (1).png", "motilal_t.png"),
    ("Ajanta-Pharma-Limited-Logo.jpg", "ajanta_t.png"),
    ("download.png", "rotary_t.png"),
]

for src, dst in jobs:
    remove_white_bg(src, dst)
