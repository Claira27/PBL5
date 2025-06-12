import os
import cv2
import numpy as np
from glob import glob
from concurrent.futures import ThreadPoolExecutor

# 1. RGB → Class ID Mapping
color_to_class = {
    (140, 140, 200): 1,  # Crosswalk - Plain
    (200, 128, 128): 1,  # Lane Marking - Crosswalk
    (128,  64, 128): 2,  # Road
    (128,  64, 255): 2,  # Bike Lane
    (96,   96,  96): 3,  # Pedestrian Area
    (244,  35, 232): 3   # Sidewalk
}
# 2. Chuyển 1 mask
def process_mask(mask_path):
    filename = os.path.basename(mask_path)
    save_path = os.path.join(output_mask_dir, filename)

    mask_rgb = cv2.imread(mask_path)
    mask_rgb = cv2.cvtColor(mask_rgb, cv2.COLOR_BGR2RGB)

    h, w, _ = mask_rgb.shape
    mask_class = np.full((h, w), 4, dtype=np.uint8)  # Default: background

    for color, class_id in color_to_class.items():
        match = np.all(mask_rgb == np.array(color).reshape(1, 1, 3), axis=-1)
        mask_class[match] = class_id

    cv2.imwrite(save_path, mask_class)

input_mask_dir = 'masks_resized'
output_mask_dir = 'masks_resized_integer'
os.makedirs(output_mask_dir, exist_ok=True)

mask_paths = glob(os.path.join(input_mask_dir, '*.png'))

with ThreadPoolExecutor(max_workers=8) as executor:
    list(executor.map(process_mask, mask_paths))