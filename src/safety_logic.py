def is_overlapping(worker_box, ppe_box):
    """Checks if the center of a PPE detection falls within a worker's bounding box."""
    wx1, wy1, wx2, wy2 = worker_box
    # Calculate PPE center point for spatial association
    cx = (ppe_box[0] + ppe_box[2]) / 2
    cy = (ppe_box[1] + ppe_box[3]) / 2
    # Return true if PPE center is inside worker boundaries
    return wx1 <= cx <= wx2 and wy1 <= cy <= wy2

def check_compliance(worker_box, ppe_detections):
    """Evaluates safety compliance for a single worker using a 11-class hierarchy."""
    violations = []
    found_gear = {"helmet": False, "vest": False, "gloves": False, "boots": False, "goggles": False}
    
    # Check for explicit negative class detections (Classes 7-10)
    for label, boxes in ppe_detections['negative'].items():
        for b in boxes:
            if is_overlapping(worker_box, b):
                violations.append(f"REQ: {label.replace('_', ' ').upper()}")

    # Check for positive PPE presence (Classes 0-4)
    for label, boxes in ppe_detections['positive'].items():
        for b in boxes:
            if is_overlapping(worker_box, b):
                found_gear[label] = True

    # Flag missing mandatory gear if not detected
    if not found_gear["helmet"] and "REQ: NO HELMET" not in violations:
        violations.append("MISSING: HELMET")
    if not found_gear["vest"]:
        violations.append("MISSING: VEST")
        
    return violations