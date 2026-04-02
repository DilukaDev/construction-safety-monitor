# Construction Safety Monitor

A real-time computer vision system that monitors construction site safety by detecting workers and their personal protective equipment (PPE) using YOLO11 object detection.

## Overview

- **Detects workers** in images and videos using YOLO11 object detection
- **Identifies PPE** including helmets, vests, gloves, boots, and goggles
- **Flags safety violations** when workers lack required protective equipment
- **Provides real-time alerts** through an interactive web interface
- **Processes both images and video** for flexible site monitoring

## Installation

### Prerequisites

- Python 3.13+
- `uv` package manager

### Setup & Usage

1. **Install dependencies**

   ```bash
   uv sync
   ```

2. **Run the application**

   ```bash
   streamlit run app.py
   ```

   The application will open in your browser (http://localhost:8501)

## Project Structure

```
construction-safety-monitor/
├── README.md
├── .python-version           # Python version specification
├── pyproject.toml            # Project configuration and dependencies
├── uv.lock                   # Locked dependency versions
├── app.py                    # Main Streamlit application
├── docs/
│   ├── dataset.md            # Dataset composition and engineering
│   └── safety_protocols.md   # Safety compliance rules and logic
├── src/
│   ├── __init__.py           # Package initialization
│   ├── process_logic.py      # Frame processing and YOLO inference
│   └── safety_logic.py       # Safety compliance checking logic
├── models/
│   └── best.pt               # Trained YOLO11 model weights
├── notebooks/
│   └── Construction_Safety_Model_Development.ipynb  # Model training notebook
└── reports/                  # Output reports and analysis results
```

## Model Performance

The YOLO11 detection model achieves the following results on test data:

| Metric    | Score  |
| --------- | ------ |
| mAP50     | 0.5427 |
| Precision | 0.5835 |
| Recall    | 0.5294 |

## Dataset & Training Results

The dataset and full training results can be accessed from the following link:

[Google Drive - Construction Safety Project](https://drive.google.com/drive/folders/1WghXGIxs1gqLmr_FD0uk5Xu7MZ-46856?usp=sharing)