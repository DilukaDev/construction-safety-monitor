import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import tempfile
from PIL import Image
from src.process_logic import process_frame

st.set_page_config(page_title="Safety Monitor", layout="wide")
st.title("Construction Safety Monitor")

@st.cache_resource
def load_model():
    return YOLO("models/best.pt")

try:
    model = load_model()
    CLASS_NAMES = model.names 
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

source_type = st.sidebar.radio("Input Source", ("Image", "Video"))

# Image processing
if source_type == "Image":
    uploaded_file = st.file_uploader("Upload Site Photo", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        processed = process_frame(frame, model, CLASS_NAMES)
        st.image(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB), width='stretch')

# Video processing
elif source_type == "Video":
    uploaded_video = st.file_uploader("Upload Footage", type=["mp4", "mov"])
    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())
        cap = cv2.VideoCapture(tfile.name)
        st_frame = st.empty()
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret: break
            processed = process_frame(frame, model, CLASS_NAMES)
            st_frame.image(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB), width='stretch')
        cap.release()