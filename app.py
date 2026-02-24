import tkinter as tk 
from PIL import Image, ImageDraw, ImageOps, ImageFilter 
import numpy as np 
import tensorflow as tf 
 
# Load model 
model = tf.keras.models.load_model("my_model.keras") 
 
# Main window 
window = tk.Tk() 
window.title("MNIST Digit Recognizer") 
window.geometry("420x550") 
window.configure(bg="#222") 
 
# Canvas 
canvas = tk.Canvas(window, width=280, height=280, bg='black', highlightthickness=0) 
canvas.pack(pady=20) 
 
# PIL image 
image = Image.new("L", (280, 280), "black") 
draw = ImageDraw.Draw(image) 
 
# Drawing 
def draw_lines(event): 
    x, y = event.x, event.y 
    r = 10 
    canvas.create_oval(x-r, y-r, x+r, y+r, fill='white', outline='white') 
    draw.ellipse([x-r, y-r, x+r, y+r], fill='white') 
 
canvas.bind("<B1-Motion>", draw_lines) 
 
# 🔥 Predict automatically when mouse released 
canvas.bind("<ButtonRelease-1>", lambda event: predict_digit()) 
 
# Clear 
def clear_canvas(): 
    canvas.delete("all") 
    draw.rectangle([0, 0, 280, 280], fill="black") 
    result_label.config(text="Prediction: ") 
 
# Preprocess image 
def preprocess_image(img): 
 
    # resize to 28
    img = img.resize((28, 28), Image.Resampling.LANCZOS) 
 
    # convert numpy 
    img_array = np.array(img) 
 
    # normalize 
    img_array = img_array.astype("float32") / 255.0 
 
    # flatten 
    img_array = img_array.reshape(1, 784) 
 
    return img_array 
 
# Predict 
def predict_digit(): 
 
    processed = preprocess_image(image) 
    prediction = model.predict(processed, verbose=0) 
 
    digit = np.argmax(prediction) 
    confidence = np.max(prediction) * 100 
 
    result_label.config( 
        text=f"Prediction: {digit}  ({confidence:.2f}%)" 
    ) 
 
 
clear_btn = tk.Button( 
    window, text="Clear", 
    command=clear_canvas, 
    bg="#f44336", fg="white", 
    font=("Arial", 12), width=15 
) 
clear_btn.pack() 
 
# Result label 
result_label = tk.Label( 
    window, 
    text="Prediction: ", 
    font=("Arial", 20), 
    bg="#222", 
    fg="white" 
) 
result_label.pack(pady=30) 
 
window.mainloop()