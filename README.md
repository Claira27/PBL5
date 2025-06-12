# Dự án Giám sát Đường đi & Nhận diện Vật cản

Hệ thống sử dụng hai mô hình AI chạy song song để đảm bảo an toàn cho người/thú cưng/robot di chuyển trên đường:
1. **Nhận diện vật cản** bằng YOLOv8n (object detection).
2. **Phân làn đường đi** bằng DeepLabV3+ với backbone MobileNetV2 (semantic segmentation).
# PBL5

---

## 1. Nhận diện vật cản bằng YOLOv8n

- **Mô hình**: YOLOv8n (phiên bản nhẹ)
- **Đầu vào**: ảnh
- **Đầu ra**: Bounding boxes và nhãn đối tượng
- **Ứng dụng**: Phát hiện vật cản như người, xe, vật thể cản đường → cảnh báo sớm

### File chính:
- `detect.py`: Nhận diện vật thể và phát cảnh báo
- `model.pt`: Trọng số mô hình đã được huấn luyện (hoặc fine-tune)

### Cách chạy:
```bash
python yolo/test/detect.py --source 0 --weights yolo/test/model.pt

---

## 2. Phân làn đường đi bằng DeepLabV3+ (MobileNetV2)
- **Mô hình**: YOLOv8n (phiên bản nhẹ)
- **Đầu vào**: ảnh
- **Đầu ra**: Bounding boxes và nhãn đối tượng
- **Lớp phân đoạn**: Vỉa hè, làn đường, vạch kẻ qua đường cho người đi bộ, nền
- **Ứng dụng**: Xác định người đang đi đúng làn an toàn không

### File chính:
Deeplabv3_train.ipynb: Kết quả train và test với ảnh 
deeplabv3plus_best.pth: Trọng số mô hình huấn luyện 4 lớp

##Yêu cầu cài đặt
pip install -r requirements.txt
