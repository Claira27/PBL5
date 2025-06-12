import cv2
import os
from glob import glob
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

input_image_dir = 'mask'
input_mask_dir = 'temp'

output_image_dir = 'images_resized'
output_mask_dir = 'masks_resized'

resize_width, resize_height = 512, 384

os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_mask_dir, exist_ok=True)

image_paths = sorted(glob(os.path.join(input_image_dir, '*.jpg')))
mask_paths = sorted(glob(os.path.join(input_mask_dir, '*.png')))

def process_pair(img_path, mask_path):
    img = cv2.imread(img_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_UNCHANGED)

    img_resized = cv2.resize(img, (resize_width, resize_height), interpolation=cv2.INTER_AREA)
    mask_resized = cv2.resize(mask, (resize_width, resize_height), interpolation=cv2.INTER_NEAREST)

    filename = os.path.basename(img_path)
    maskname = os.path.basename(mask_path)

    cv2.imwrite(os.path.join(output_image_dir, filename), img_resized)
    cv2.imwrite(os.path.join(output_mask_dir, maskname), mask_resized)

# Dùng ThreadPoolExecutor để xử lý đa luồng
with ThreadPoolExecutor(max_workers=8) as executor:
    list(tqdm(executor.map(lambda args: process_pair(*args), zip(image_paths, mask_paths)), total=len(image_paths)))
