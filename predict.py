from ultralytics import YOLO
import cv2

model_path = '/content/drive/MyDrive/ColabNotebooks/Heavy Vehicle Detection/runs/segment/train2/weights/last.pt'
image_path = '/content/drive/MyDrive/ColabNotebooks/Heavy Vehicle Detection/valid/images/Ch1_20220924070000-1-_mp4-228_jpg.rf.1f5263334d7f1c4c54b7681ecb109ab1.jpg'

img = cv2.imread(image_path)
H, W, _ = img.shape

model = YOLO(model_path)

results = model(img)

for result in results:
  for mask in result.masks.data:
    mask = mask.to('cpu').numpy() * 255
    mask = cv2.resize(mask, (W, H))
    cv2.imwrite('./Ch1_20220924070000-1-_mp4-228_jpg.rf.1f5263334d7f1c4c54b7681ecb109ab1.png', mask)
