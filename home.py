import streamlit as st
import sys
import os

# Dynamically add the yolov5 directory to sys.path
yolov5_path = os.path.join(os.path.dirname(__file__), 'yolov5')
if yolov5_path not in sys.path:
    sys.path.append(yolov5_path)

# Set Streamlit page configuration
st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')

# Page title and caption
st.title("YOLO V5 Object Detection App")
st.caption('This web application demonstrates Object Detection')

# Content
st.markdown("""
### This App detects weapons from Images
- [Click here for Image Detection](/Image_detection/)  
- [Click here for Real Time Detection](/Real_time_detection/)  

The app detects 3 objects: 
1. gun - רובה ארוך
2. knife - סכין
3. pistol - אקדח
""")
