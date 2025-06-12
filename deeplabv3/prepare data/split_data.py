import os
import shutil
from glob import glob
from sklearn.model_selection import train_test_split

# Thư mục gốc chứa ảnh và mask
image_dir = 'images_resized'
mask_dir = 'masks_resized'

# Thư mục lưu kết quả chia
output_dir = 'data1'
train_img_dir = os.path.join(output_dir, 'train/images')
train_mask_dir = os.path.join(output_dir, 'train/masks')
val_img_dir = os.path.join(output_dir, 'val/images')
val_mask_dir = os.path.join(output_dir, 'val/masks')
test_img_dir = os.path.join(output_dir, 'test/images')
test_mask_dir = os.path.join(output_dir, 'test/masks')

# Tạo các thư mục nếu chưa có
for d in [train_img_dir, train_mask_dir, val_img_dir, val_mask_dir, test_img_dir, test_mask_dir]:
    os.makedirs(d, exist_ok=True)

# Lấy danh sách ảnh và mask (sắp xếp để đảm bảo đúng cặp)
img_paths = sorted(glob(os.path.join(image_dir, '*.jpg')))  # hoặc .png tùy file
mask_paths = sorted(glob(os.path.join(mask_dir, '*.png')))

# Kiểm tra số lượng ảnh và mask phải bằng nhau
assert len(img_paths) == len(mask_paths), "Số ảnh và mask không bằng nhau!"

# Chia train (70%) và temp (30%)
train_imgs, temp_imgs, train_masks, temp_masks = train_test_split(
    img_paths, mask_paths, test_size=0.3, random_state=42)

# Chia val và test từ phần temp (15% val, 15% test)
val_imgs, test_imgs, val_masks, test_masks = train_test_split(
    temp_imgs, temp_masks, test_size=0.5, random_state=42)

# Hàm copy ảnh và mask vào thư mục tương ứng
def copy_files(img_list, mask_list, img_dest, mask_dest):
    for img_path, mask_path in zip(img_list, mask_list):
        shutil.copy(img_path, img_dest)
        shutil.copy(mask_path, mask_dest)

# Copy từng phần
copy_files(train_imgs, train_masks, train_img_dir, train_mask_dir)
copy_files(val_imgs, val_masks, val_img_dir, val_mask_dir)
copy_files(test_imgs, test_masks, test_img_dir, test_mask_dir)

print(f"Train: {len(train_imgs)} ảnh")
print(f"Val: {len(val_imgs)} ảnh")
print(f"Test: {len(test_imgs)} ảnh")
