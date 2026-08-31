import sys
import numpy as np
from PIL import Image
from skimage.segmentation import flood

def remove_white_bg(path_in, path_out, tol=18, feather=2):
    img = Image.open(path_in).convert("RGB")
    arr = np.array(img).astype(np.int16)
    # "whiteness" mask: how close each pixel is to pure white
    dist = np.sqrt(((arr - 255) ** 2).sum(axis=2))
    is_white = dist < (tol * 3)

    h, w = is_white.shape
    mask = np.zeros((h, w), dtype=bool)
    # flood fill from all border seed points that are white
    border_points = []
    for x in range(w):
        border_points.append((0, x))
        border_points.append((h - 1, x))
    for y in range(h):
        border_points.append((y, 0))
        border_points.append((y, w - 1))

    visited = np.zeros((h, w), dtype=bool)
    for (y, x) in border_points:
        if is_white[y, x] and not visited[y, x]:
            region = flood(is_white, (y, x), tolerance=0)
            mask |= region
            visited |= region

    alpha = np.where(mask, 0, 255).astype(np.uint8)

    # feather the edge slightly so it's not razor-sharp / jaggy
    from scipy.ndimage import gaussian_filter
    alpha_soft = gaussian_filter(alpha.astype(np.float32), sigma=feather)
    alpha_soft = np.clip(alpha_soft, 0, 255).astype(np.uint8)

    rgba = np.dstack([np.array(img), alpha_soft])
    out = Image.fromarray(rgba, mode="RGBA")
    out.save(path_out)
    print(f"{path_in} -> {path_out}  size={out.size}")

if __name__ == "__main__":
    # 使い方:
    #   python3 remove_bg.py 入力画像.jpg assets/costume/school.png
    #
    # 白背景の一枚絵を透過PNGに変換します。
    # 輪郭に白い縁が残る場合は tol を小さく（例: 10）、
    # 逆に背景が残る場合は大きく（例: 30）してみてください。
    if len(sys.argv) < 3:
        print("usage: python3 remove_bg.py <input_image> <output.png> [tol]")
        sys.exit(1)

    src = sys.argv[1]
    dst = sys.argv[2]
    tol = int(sys.argv[3]) if len(sys.argv) > 3 else 18
    remove_white_bg(src, dst, tol=tol)
