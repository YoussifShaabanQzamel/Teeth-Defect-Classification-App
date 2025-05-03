import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("mymodel.h5")  

model=load_model()

class_names=["CaS", "CoS", "Gum", "MC", "OC", "OLP", "OT"]  

def preprocess_image(image):
    image=image.resize((224,224)) 
    image=np.array(image) / 255.0  
    return np.expand_dims(image, axis=0)  

st.title("Teeth Defect Classification")
st.write("Upload an image of a tooth defect to classify it.")
uploaded_file = st.file_uploader("Choose an image...",type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    processed_image = preprocess_image(image)
    predictions=model.predict(processed_image)
    predicted_class_index=np.argmax(predictions[0])  
    predicted_class_name=class_names[predicted_class_index]
    confidence=np.max(predictions[0])*100  
    st.subheader(f"Prediction: {predicted_class_name}")
    st.write(f"Confidence: {confidence:.2f}%")
