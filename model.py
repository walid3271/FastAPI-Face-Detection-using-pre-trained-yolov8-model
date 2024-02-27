from ultralytics import YOLO
Model = YOLO('Code/AI_Model/facev8.pt')

# import torch
# Model = torch.hub.load('./yolov5', 'custom', path='./AI_Model/yolov5.pt', source='local')