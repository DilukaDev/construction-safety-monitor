import cv2
from .safety_logic import check_compliance

def process_frame(frame, model, class_names):
    """Detects workers and PPE to render safety compliance alerts on a frame."""
    # Run YOLO11 inference with confidence threshold
    results = model(frame, conf=0.5, verbose=False)[0]
    
    workers = []
    ppe_data = {
        'positive': {"helmet": [], "gloves": [], "vest": [], "boots": [], "goggles": []},
        'negative': {"no_helmet": [], "no_goggle": [], "no_gloves": [], "no_boots": []}
    }

    # Group detections into workers and PPE categories
    for box in results.boxes:
        cls = int(box.cls[0])
        label = class_names[cls]
        coords = box.xyxy[0].tolist()
        
        if label == "Person":
            workers.append(coords)
        elif label in ppe_data['positive']:
            ppe_data['positive'][label].append(coords)
        elif label in ppe_data['negative']:
            ppe_data['negative'][label].append(coords)

    unsafe_count = 0
    # Evaluate each detected worker for safety compliance
    for p_box in workers:
        violations = check_compliance(p_box, ppe_data)
        is_safe = len(violations) == 0
        
        color = (0, 255, 0) if is_safe else (0, 0, 255)
        label_text = "SAFE" if is_safe else "VIOLATION"
        
        # Draw worker bounding box and status label
        x1, y1, x2, y2 = map(int, p_box)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)
        cv2.putText(frame, label_text, (x1, max(25, y1 - 10)), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        
        # List specific PPE violations below the worker box
        if not is_safe:
            unsafe_count += 1
            for i, v_text in enumerate(violations):
                cv2.putText(frame, v_text, (x1, y2 + 20 + (i*20)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    # Display aggregate site status and total violation count
    status = "SAFE" if unsafe_count == 0 else "UNSAFE"
    s_color = (0, 255, 0) if unsafe_count == 0 else (0, 0, 255)
    cv2.rectangle(frame, (0, 0), (450, 60), (255, 255, 255), -1)
    cv2.putText(frame, f"SITE: {status} | ALERTS: {unsafe_count}", 
                (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, s_color, 2)
    
    return frame