"""Tiny wrapper around a YOLOv8 model to detect lighting fixtures."""
from ultralytics import YOLO
import os

MODEL_PATH = os.getenv("MODEL_PATH", "models/light_yolov8.pt")

# Load once
model = YOLO(MODEL_PATH)

def detect_lights(img_path: str) -> dict:
    """Detect fixtures & return their boxes + count"""
    results = model(img_path)
    boxes = results[0].boxes

    detections = []
    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
        conf = float(box.conf[0])
        detections.append({
            "id": i + 1,
            "bbox": [float(x1), float(y1), float(x2), float(y2)],
            "confidence": conf
        })
    return {"count": len(detections), "detections": detections}