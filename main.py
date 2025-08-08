import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import io
from tensorflow.keras.models import load_model

model = load_model('cifar10_model.keras')
app = FastAPI()

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image = image.resize((32, 32))
    image_array = np.array(image)/255.0
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    return image_array
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    content = await file.read()
    image_array = preprocess_image(content) # Preprocess the image
    predictions = model.predict(image_array)
    predicted_class = class_names[np.argmax(predictions[0])] # Get the class with the highest probability
    return JSONResponse(content={"class": predicted_class})
@app.get("/")
async def root():
    return {"message": "Welcome to the CIFAR-10 image classification API. Upload an image to get predictions."}

