# 🍌 Banana Leaf Disease Detection and Recommendation System

An AI-powered agricultural tool that detects banana leaf diseases and provides tailored treatment, management, and prevention recommendations.

---

## 📌 Features

- **Leaf Verification**: Checks if the uploaded image is indeed a banana leaf using an out-of-distribution (OOD) threshold.
- **Multi-Class Disease Classification**:
  - `Black Sigatoka`
  - `Fusarium Wilt`
  - `Healthy`
  - `Not Banana Leaf` (Out-of-distribution filter)
- **Actionable Recommendations**: Detailed symptoms, disease background, cultural/chemical management techniques, and preventive measures.
- **User-Friendly Web Interface**: Built with Streamlit for quick and responsive diagnosis.
- **RESTful API**: Flask backend providing modular endpoints for inference and integration.
- **High Diagnostic Accuracy**: Fine-tuned MobileNetV2 architecture achieving **99% accuracy** across 3,350+ validation images.
- **🐳 Docker Containerized**: Production-ready multi-container setup via Docker & Docker Compose.

---

## 📊 Project Milestones & Status (90% Complete)

- ✅ **Unified 4-Class Classification**: Integrated Out-of-Distribution (`Not_Banana_Leaf`) rejection filter.
- ✅ **Backend Integration**: Flask REST API server (`/predict` & `/health`) serving model inference and recommendation payloads.
- ✅ **Frontend Dashboard**: Responsive 2-column Streamlit web application connected asynchronously to backend services.
- ✅ **Docker Containerization**: Full Docker Compose setup for microservices architecture.
- ⏳ **Upcoming (Reporting 10)**: Interactive farm analytics dashboard and final project defense documentation.

---

## 🏗️ Project Architecture

```
Banana Leaf Disease Project/
│
├── backend/
│   ├── models/                  # Saved Keras model artifacts (e.g. unified_finetune_latest.keras)
│   ├── app.py                   # Flask API entry point (endpoints: /predict, /health)
│   ├── model_utils.py           # Single-pass preprocessing & inference logic
│   ├── recommendations.py       # Disease advisory & management knowledge base
│   ├── requirements.txt         # Backend dependencies
│   ├── Dockerfile               # Backend container configuration
│   └── .dockerignore            # Backend ignore rules
│
├── frontend/
│   ├── streamlit_app.py         # Streamlit 2-column responsive UI
│   ├── requirements.txt         # Frontend dependencies
│   ├── Dockerfile               # Frontend container configuration
│   └── .dockerignore            # Frontend ignore rules
│
├── notebooks/                   # Training & experimentation notebooks
├── output/                      # Evaluation plots & confusion matrix metrics
├── docker-compose.yml           # Multi-container Docker orchestration
├── .dockerignore                # Root Docker ignore rules
├── requirements.txt             # Project-wide dependencies
├── .gitignore                   # Ignored files & cache
└── README.md                    # Project documentation
```

---

## 🐳 Running with Docker (Recommended)

The easiest and cleanest way to run the entire stack is using **Docker Compose**.

### Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (includes Docker Compose).

### 1. Build and Launch Containers
From the project root directory, run:

```bash
docker-compose up --build
```

Docker will build the backend and frontend container images, start both services, and perform health checks automatically.

### 2. Access the Application
- 🌐 **Frontend UI (Streamlit)**: [http://localhost:8501](http://localhost:8501)
- 🔌 **Backend API (Flask)**: [http://localhost:5000](http://localhost:5000)
- 🩺 **Backend Health Check**: [http://localhost:5000/health](http://localhost:5000/health)

### 3. Stop Containers
To stop and remove running containers, run:

```bash
docker-compose down
```

---

## 💻 Local Setup (Without Docker)

If you prefer to run the application directly on your local system using Python:

### 1. Clone the Repository
```bash
git clone https://github.com/jayeshuttale/banana-leaf-disease-detection-and-recommendation-system.git
cd banana-leaf-disease-detection-and-recommendation-system
```

### 2. Environment Setup & Installation
Create a virtual environment and install the dependencies:

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
Ensure trained model file (e.g. `unified_finetune_latest.keras` or `unified_best_model.keras`) is located in the `backend/models/` directory.

### 4. Start the Application

#### Step 1: Start the Backend (Flask API)
```bash
cd backend
python app.py
```
*The Flask API runs on `http://localhost:5000`.*

#### Step 2: Start the Frontend (Streamlit)
In a separate terminal window:
```bash
cd frontend
streamlit run streamlit_app.py
```
*The Streamlit web UI launches at `http://localhost:8501`.*

---

## ⚙️ Environment Variables

| Variable | Description | Default | Service |
| :--- | :--- | :--- | :--- |
| `PORT` | Backend Flask server port | `5000` | Backend |
| `FLASK_DEBUG` | Enable Flask debug mode | `False` | Backend |
| `BACKEND_URL` | Flask prediction endpoint URL for frontend | `http://127.0.0.1:5000/predict` | Frontend |

---

## 🛠️ Tech Stack

- **Deep Learning**: TensorFlow / Keras (MobileNetV2 architecture)
- **Backend API**: Flask REST API
- **Frontend UI**: Streamlit (Responsive wide layout)
- **Containerization**: Docker, Docker Compose
- **Image Processing**: Pillow, NumPy
- **Languages & Tools**: Python 3.10+, Git

---

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
