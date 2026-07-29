# AIOps Platform 🚀

An end-to-end Machine Learning Operations (MLOps) platform built using FastAPI, Docker, MLflow, DVC, and Scikit-learn. It enables dataset upload, model training, prediction, and experiment tracking through REST APIs.

## Features

- 📂 Dataset Upload API
- 🤖 Model Training
- 📊 Prediction API
- 📈 MLflow Experiment Tracking
- 🐳 Docker Support
- ⚡ FastAPI Backend

## Tech Stack

- FastAPI
- Python
- Scikit-learn
- LightGBM
- MLflow
- DVC
- Docker

## Run Locally

```bash
git clone https://github.com/<your-username>/AIOps-Platform.git
cd AIOps-Platform
pip install -r requirements.txt
python run.py
```

Open:

```
http://127.0.0.1:8000/docs
```

## Docker

```bash
docker build -t aiops-platform .
docker run -p 8000:8000 aiops-platform
```

## Project Structure

```
app/
ml/
datasets/
models/
config/
deployment/
monitoring/
run.py
requirements.txt
Dockerfile
```

## Future Improvements

- User Authentication
- Model Versioning
- CI/CD Pipeline
- Cloud Deployment
- Real-time Monitoring

## Author

**Nikhitha**
