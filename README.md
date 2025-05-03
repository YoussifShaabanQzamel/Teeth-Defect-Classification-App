# 🦷 Teeth Defect Classification App

A lightweight and interactive web app that detects and classifies **teeth defects** from **normal (non-X-ray) teeth images** using a deep learning model based on **MobileNetV2**. Built and deployed with **Streamlit** for seamless user interaction.

---

## 🎥 Demo

[![Watch the demo](https://img.shields.io/badge/▶️%20Watch%20Demo-Click%20Here-blue)](https://drive.google.com/file/d/1mXJF9WPDwUBScqout8YQNMxHYu_5l4Yz/view?usp=sharing)

---

## 🚀 Features

- 📸 Upload clear, non-X-ray teeth images
- ⚡ Fast real-time prediction using MobileNetV2
- 🌐 Easy-to-use web interface built with Streamlit
- 💡 Visual and intuitive result display

---

## 🧠 Model Details

- **Architecture**: MobileNetV2 (pretrained on ImageNet)
- **Dataset**: Custom images of normal teeth with defect annotations
- **Training**: Fine-tuned on labeled defect types
- **Preprocessing**: Resizing, normalization, and augmentation

---

## 🛠️ Tech Stack

| Component      | Technology          |
|----------------|---------------------|
| Model          | TensorFlow / Keras  |
| Architecture   | MobileNetV2         |
| Web Framework  | Streamlit           |
| Language       | Python              |
| Deployment     | Streamlit Cloud / Localhost |

---

## 📁 Project Structure
### The project is organized as follows:
### teeth-defect-classifier/
#### ├── app.py                # Main Streamlit app to run the web interface
#### ├── pretrained-mobilnetv2.ipynb                # Model Training and Preprocessing Code 
#### ├── model.h5              # Trained model file
#### └── README.md             # Project documentation (this file)
