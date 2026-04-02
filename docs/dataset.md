# Dataset Documentation: Construction-PPE (Enhanced)

This project utilizes an augmented version of the Ultralytics Construction-PPE dataset, specifically modified to improve real-world reliability and class balance.

## Dataset Composition

The final dataset consists of a mixture of high-quality synthetic data and manual site captures to ensure the model performs across various environmental conditions.

### Dataset Split

| Component      | Count | Percentage |
| -------------- | ----- | ---------- |
| Total Images   | 1,436 | 100%       |
| Training Set   | 1,148 | 80%        |
| Validation Set | 145   | 10%        |
| Testing Set    | 143   | 10%        |

## Data Engineering & Augmentation

To move from a baseline model to a production-ready system, the following modifications were performed:

### Sourcing

Combined the base Ultralytics PPE dataset with 20+ custom records sourced from real-world construction site footage and the Roboflow Construction Site Safety dataset.

### Labeling (CVAT)

Used CVAT (Computer Vision Annotation Tool) to manually label new records and correct existing bounding boxes for better precision.

### Class Balancing

Specifically targeted "Minority Classes" (e.g., no_goggle, no_boots) to reduce class imbalance, ensuring the model is equally sensitive to all types of safety violations.

## Class Definitions (11 Classes)

The model is trained to detect and distinguish between the following categories:

| ID   | Class Name                                | Description                            |
| ---- | ----------------------------------------- | -------------------------------------- |
| 0-4  | helmet, gloves, vest, boots, goggles      | Standard Compliant PPE                 |
| 5    | none                                      | General objects/Background             |
| 6    | Person                                    | Human detection (Anchor for PPE check) |
| 7-10 | no_helmet, no_goggle, no_gloves, no_boots | Safety Violations (Critical)           |
