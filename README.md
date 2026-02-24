# 🧠 Handwritten Digit Recognition System (MNIST + Keras + Tkinter)

An end-to-end deep learning project that trains a neural network on the MNIST dataset and deploys it into a real desktop application for real-time handwritten digit prediction.

---

## 🚀 Project Overview

This project consists of two main parts:

1. 📊 Training a Neural Network on MNIST using Keras
2. 🖥️ Building a Desktop Application using Tkinter for live digit recognition

The model achieves ~98% accuracy on the MNIST test dataset.

---

## 📂 Project Structure

├── Mnist_with_keras.ipynb   # Model training notebook  
├── my_model.keras           # Saved trained model  
├── app.py                   # Desktop GUI application  
└── README.md  

---

## 📊 Part 1: Model Training (MNIST + Keras)

In the notebook:

- Loaded MNIST dataset
- Visualized sample digits
- Applied preprocessing:
  - Flattened images (28x28 → 784)
  - Normalized pixel values (0–255 → 0–1)
  - One-hot encoded labels
- Built a Fully Connected Neural Network:
  - Dense(64, ReLU)
  - Dense(64, ReLU)
  - Dense(10, Softmax)
- Used:
  - Optimizer: Adam
  - Loss: Categorical Crossentropy
- Evaluated on test data (~98% accuracy)
- Saved the trained model as `my_model.keras`

---

## 🖥️ Part 2: Desktop Application (Tkinter)

The `app.py` file:

- Loads the trained model
- Provides a drawing canvas (280x280)
- Automatically predicts when mouse is released
- Preprocesses drawing:
  - Resize to 28x28
  - Normalize
  - Flatten to (1, 784)
- Displays:
  - Predicted digit
  - Confidence percentage
- Includes a Clear button

This transforms the ML model into a real interactive application.

---

## 🧪 Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- Tkinter
- Pillow (PIL)

---

## ▶️ How to Run

### 1️⃣ Train the Model
Run the notebook:


### 2️⃣ Run the App
Make sure `my_model.keras` is in the same directory as `app.py`, then run:



---

## 💡 Key Learning Outcomes

- Building a complete ML pipeline
- Understanding preprocessing for image classification
- Deploying a trained model into a real GUI application
- Connecting Deep Learning with software engineering

---

## 📌 Future Improvements

- Convert model to CNN for higher accuracy
- Add probability visualization (bar chart)
- Deploy as a web app using Gradio or Streamlit
- Improve stroke preprocessing

---

## 👨‍💻 Author

Omar Tarek  
AI & Machine Learning Enthusiast
