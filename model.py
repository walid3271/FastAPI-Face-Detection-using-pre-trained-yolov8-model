from ultralytics import YOLO
Model = YOLO('FastAPI-Object-Detection-using-pre-trained-yolov8-model/AI_Model/your_model.pt')

# import torch
# Model = torch.hub.load('./yolov5', 'custom', path='./AI_Model/yolov5.pt', source='local')
