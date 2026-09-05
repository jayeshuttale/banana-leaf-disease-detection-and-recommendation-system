# 🍌 Banana Leaf Disease Detection and Recommendation System

An AI-powered agricultural tool that detects banana leaf diseases and provides tailored treatment, management, and prevention recommendations.

---

## 📌 Features

- **Leaf Verification**: Checks if the uploaded image is indeed a banana leaf.
- **Multi-Class Disease Classification**:
  - `Black Sigatoka`
  - `Fusarium Wilt`
  - `Healthy`
  - `Not Banana Leaf` (Out-of-distribution filter)
- **Actionable Recommendations**: Detailed symptoms, disease background, cultural/chemical management techniques, and preventive measures.
- **User-Friendly Web Interface**: Built with Streamlit for quick and responsive diagnosis.
- **RESTful API**: Flask backend providing modular endpoints for inference and integration.
- **High Diagnostic Accuracy**: Fine-tuned MobileNetV2 architecture achieving **99% accuracy** across 3,350+ validation images.

---

## 📊 Project Milestones & Status (85% Complete)

- ✅ **Unified 4-Class Classification**: Integrated Out-of-Distribution (`Not_Banana_Leaf`) rejection filter.
- ✅ **Backend Integration**: Flask REST API server (`/predict`) serving model inference and recommendation payloads.
- ✅ **Frontend Dashboard**: Responsive Streamlit web application connected asynchronously to backend services.
- ⏳ **Upcoming (Reporting 9 & 10)**: Interactive farm analytics dashboard and final project defense documentation.

---

## 🏗️ Project Architecture

```
Banana Leaf Disease Project/
│
├── backend/
│   ├── models/                  # Saved Keras model (e.g. unified_best_model.keras)
│   ├── app.py                   # Flask API entry point
│   ├── model_utils.py           # Preprocessing & inference logic
│   ├── recommendations.py       # Disease advisory & management guidance
│   └── requirements.txt         # Backend dependencies
│
├── frontend/
│   ├── streamlit_app.py         # Streamlit UI
│   └── requirements.txt         # Frontend dependencies
│
├── notebooks/
│   ├── Colab books/             # Training & experimentation notebooks
│   └── PDF/                     # Documentation & reports
│
├── requirements.txt             # Project-wide dependencies
├── .gitignore                   # Ignored files & cache
└── README.md                    # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/jayeshuttale/banana-leaf-disease-detection-and-recommendation-system.git
cd banana-leaf-disease-detection-and-recommendation-system
```

### 2. Environment Setup & Installation
Create a virtual environment and install the required dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 3. Model Weights
Place the trained model file `unified_best_model.keras` inside the `backend/models/` folder.

---

## 💻 Running the Application

### Step 1: Start the Backend (Flask API)
```bash
cd backend
python app.py
```
*The Flask API will run on `http://localhost:5000`.*

### Step 2: Start the Frontend (Streamlit)
In a new terminal window:
```bash
cd frontend
streamlit run streamlit_app.py
```
*The Streamlit web UI will launch in your default browser at `http://localhost:8501`.*

---

## 🛠️ Tech Stack

- **Deep Learning**: TensorFlow / Keras (MobileNetV2 architecture)
- **Backend API**: Flask
- **Frontend UI**: Streamlit
- **Image Processing**: Pillow, NumPy
- **Languages & Tools**: Python 3.10+, Git

---

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
