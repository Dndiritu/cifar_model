CIFAR-10 CNN Image Classification (with FastAPI Deployment)
markdown
Copy
Edit
# 🖼️ CIFAR-10 Image Classification with CNN (FastAPI Deployment)

This project uses a **Convolutional Neural Network (CNN)** to classify images from the **CIFAR-10 dataset** into 10 categories.  
The trained model is deployed using **FastAPI**, allowing predictions to be made via a REST API.

---

## 📂 Dataset

The [CIFAR-10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html) consists of **60,000 color images** (32x32 pixels) in **10 classes**:
- Airplane ✈️
- Automobile 🚗
- Bird 🐦
- Cat 🐱
- Deer 🦌
- Dog 🐶
- Frog 🐸
- Horse 🐎
- Ship 🚢
- Truck 🚚

The dataset is automatically downloaded via `tensorflow.keras.datasets`.

---

## 🛠️ Technologies Used
- **Python 3.x**
- **TensorFlow / Keras**
- **FastAPI** (model deployment)
- **Uvicorn** (ASGI server)
- **NumPy**
- **Pillow** (image processing)
- **Matplotlib** & **Seaborn** (visualization)

---

## 📜 Project Structure

├── cifar10_cnn.py # Model training & evaluation
├── main.py # FastAPI app for serving predictions
├── requirements.txt # Required dependencies
├── README.md # Project documentation
└── saved_model/ # Directory to save trained models

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/cifar10-cnn-fastapi.git
cd cifar10-cnn-fastapi
Create a virtual environment

python -m venv venv
venv\Scripts\activate        # Windows
Install dependencies

pip install -r requirements.txt
🏗️ Model Training
To train the model and save it:

bash
Copy
Edit
python cifar10_cnn.py
The trained model will be saved in the saved_model/ directory.

🚀 Running the API
Start the FastAPI server:

bash
Copy
Edit
uvicorn main:app --reload
API will be available at:

http://127.0.0.1:8000
📡 API Endpoints
1️⃣ Root Endpoint
GET /
Returns a welcome message.

2️⃣ Predict Endpoint
POST /predict
Accepts an image file and returns the predicted CIFAR-10 class.

Request Example (via cURL):

📊 Training & Results
Loss function: categorical_crossentropy

Optimizer: Adam

Epochs: 10–50 (tune as needed)

Batch size: 64

Accuracy Achieved: ~70%

🧠 Key Learnings
Combining CNNs with FastAPI enables real-time image classification via REST API.

Proper preprocessing of input images is crucial for accurate predictions.

Dropout helps reduce overfitting in CNN models.

📜 License
This project is licensed under the MIT License.

✨ Author
David Ndiritu Mwaniki
📧 davidndiritu2000@gmail.com
🔗 www.linkedin.com/in/david-ndiritu
