
# Apartment Rental Price Prediction System
Welcome to the Apartment Rental Price Prediction System repository. This project is designed to predict the rental prices of apartments using a range of apartment attributes. Utilizing the UCI Machine Learning Repository's Apartment for Rent dataset, this system offers an innovative approach to understanding rental market dynamics.
## Usage video

[AppUsage.webm](https://github.com/pedrocavalc/Apartament-Price-System/assets/89861384/5626aab9-9235-40ee-9489-c1a1503aa228)

## Features
- Rental Price Prediction: Estimate apartment rental prices based on various attributes.
- Data-Driven Insights: Gain insights into factors affecting rental prices.
- MLOps Integration: Leveraging modern MLOps tools for enhanced performance and reliability.
## Tech Stack
- Docker: For containerizing the different components of the system, ensuring consistent environments and easy deployment.
- Python: The primary programming language used for data processing and model development.
- MLFlow: For tracking experiments, model management, and registry.
- Scikit-learn: A robust library for machine learning model development.
- FastAPI: A modern, fast web framework for building APIs.
- Streamlit: For creating interactive web applications for user predictions.
- Pandas: For data manipulation and analysis.
- Other data analysis and processing tools.
- 
## Quick Start
Setup: Ensure Docker is installed on your system.
``` bash
docker-compose up
```
Access the Interface: Open your browser and navigate to http://localhost:8501 for the Streamlit UI.
Making Predictions: Use the interface to input apartment attributes and receive price predictions.
MLflow Tracking: Visit http://localhost:5000 to view tracked experiments and model versions.
## Usage
The workflow involves:

Data Acquisition: Automatically downloading the dataset.
Data Processing: Cleaning and preparing data for training.
Model Training and Tracking: Using MLflow server for training and tracking models.
Frontend and Backend Integration:
Frontend: Streamlit UI for users to input data and receive predictions.
Backend: FastAPI for serving the ML model, using MLFlow registry to load and predict.
## Directory Structure
```bash
├── application/
│   ├── app/ # API
│   ├── front/ # Front-End

├── data/
│   ├── external/
│   ├── interim/
│   ├── processed/
│   ├── raw/
│   └── ...
├── mlflow-db/ - MLFlow database
│   ├── Dockerfile
│   ├── mlflow.db
│   └── ...
├── notebooks/
│   └── exploration.ipynb
└── src/ - Train and Data modules
    ├── data-pipeline/
    ├── train/
    ├── .gitignore
    ├── README.md
    └── requirements.txt
```
Development
Model Development: Python and Scikit-learn are used for developing the prediction model.

API Development with FastAPI: Serving the model for predictions.

Frontend Development with Streamlit: Interactive UI for making predictions.

Docker Integration: Ensuring seamless operation of all components.

## Contributing
Contributions are welcome! Feel free to fork this repository, open issues, or submit PRs. For significant changes, please open an issue first to discuss the proposed change.







