import os
import random
import shutil
from glob import glob

# Thư mục gốc
input_image_dir = 'images'
input_mask_dir = 'labels'

# Thư mục lưu ảnh + mask được chọn
output_image_dir = 'images_selected'
output_mask_dir = 'masks_selected'

os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_mask_dir, exist_ok=True)

# Load file, sort để chắc chắn đúng cặp
image_paths = sorted(glob(os.path.join(input_image_dir, '*.jpg')))
mask_paths = sorted(glob(os.path.join(input_mask_dir, '*.png')))

assert len(image_paths) == len(mask_paths), "Số lượng ảnh và mask không bằng nhau!"

# Lấy 5000 index ngẫu nhiên, cố định seed cho tái tạo kết quả
random.seed(42)
indices = random.sample(range(len(image_paths)), 5000)

for i in indices:
    shutil.copy(image_paths[i], output_image_dir)
    shutil.copy(mask_paths[i], output_mask_dir)
