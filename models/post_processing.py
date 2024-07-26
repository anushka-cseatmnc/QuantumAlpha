import numpy as np

def filter_detections(detections, threshold=0.5):
    return [d for d in detections if d['confidence'] > threshold]

def non_maximum_suppression(detections, iou_threshold=0.5):
    if len(detections) == 0:
        return []

    detections = sorted(detections, key=lambda x: x['confidence'], reverse=True)
    keep = []

    while detections:
        best = detections.pop(0)
        keep.append(best)

        detections = [d for d in detections if iou(best['bbox'], d['bbox']) < iou_threshold]

    return keep

def iou(bbox1, bbox2):
    x1, y1, x2, y2 = bbox1
    x1_, y1_, x2_, y2_ = bbox2

    inter_x1 = max(x1, x1_)
    inter_y1 = max(y1, y1_)
    inter_x2 = min(x2, x2_)
    inter_y2 = min(y2, y2_)

    inter_area = max(0, inter_x2 - inter_x1) * max(0, inter_y2 - inter_y1)
    bbox1_area = (x2 - x1) * (y2 - y1)
    bbox2_area = (x2_ - x1_) * (y2_ - y1_)

    return inter_area / (bbox1_area + bbox2_area - inter_area)

# Example usage
detections = [{'bbox': [50, 50, 100, 100], 'confidence': 0.6}, {'bbox': [55, 55, 100, 100], 'confidence': 0.4}]
filtered_detections = filter_detections(detections)
nms_detections = non_maximum_suppression(filtered_detections)
