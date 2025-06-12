import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu pixel mỗi lớp
class_pixels = {
    0: 148160870,
    1: 556211243,
    2: 781220558,
    3: 2058463137
}

# Tính tổng và phần trăm
total_pixels = sum(class_pixels.values())
class_ids = list(class_pixels.keys())
pixel_counts = list(class_pixels.values())
percentages = [p / total_pixels * 100 for p in pixel_counts]

# Tạo biểu đồ
plt.figure(figsize=(10, 6))
bars = plt.bar(class_ids, pixel_counts, color='skyblue')

# Ghi nhãn trên đầu cột
for bar, count, pct in zip(bars, pixel_counts, percentages):
    plt.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 1e7,
             f"{count:,}\n({pct:.1f}%)",
             ha='center', va='bottom', fontsize=10)

# Cấu hình trục
class_names = ['Vạch qua đường', 'Đường', 'Vỉa hè', 'Nền']
plt.xticks(class_ids, class_names)
plt.ylabel("Số pixel")
plt.title("Số lượng pixel theo từng lớp")
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("pixel_distribution.png", dpi=300, bbox_inches='tight')
plt.show()