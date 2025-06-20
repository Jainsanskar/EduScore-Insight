# 🎓 EduScore Insight: Predicting Student Performance

An end-to-end machine learning web application that predicts a student's math score based on demographic and academic attributes. This project demonstrates the full ML pipeline, from data ingestion to deployment via a Flask web interface.

---

## 📌 Problem Statement

Understanding the impact of socio-academic factors on student performance can guide educational strategies.  
This application predicts `math_score` based on:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

---

## 🔁 ML Pipeline Overview

1. **Problem Definition**
2. **Data Ingestion** – Load and split dataset into train/test
3. **Data Transformation** – Handle missing values, encode categorical data, and scale features using `Pipeline` & `ColumnTransformer`
4. **Model Training** – Train multiple models (Random Forest, XGBoost, CatBoost, etc.) and perform hyperparameter tuning
5. **Model Evaluation** – Select the best model using R² score
6. **Prediction Pipeline** – Build a reusable inference pipeline
7. **Web Deployment** – Deploy using Flask for real-time predictions

---

## 📁 Project Structure

EduScore-Insight/
│
├── src/
│ ├── components/
│ │ ├── data_ingestion.py
│ │ ├── data_transformation.py
│ │ └── model_trainer.py
│ ├── pipeline/
│ │ └── predict_pipeline.py
│ ├── utils.py
│ ├── logger.py
│ └── exception.py
│
├── artifacts/ # Contains preprocessor.pkl, model.pkl, train/test data
├── templates/ # HTML form for user input
├── app.py # Flask web app
├── logs/ # Logs with timestamps
├── requirements.txt
└── README.md


---

## 🧠 Technologies Used

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **CatBoost, XGBoost**
- **Flask**
- **HTML**
- **Pickle**

---

## 💻 Web Application

The app allows users to input student details through a form and returns the predicted math score in real-time.

To run:
```bash
python app.py

Visit http://127.0.0.1:5000 in your browser.


## 🧾 Artifacts
File	Description
artifacts/train.csv	Training dataset
artifacts/test.csv	Testing dataset
artifacts/preprocessor.pkl	Serialized transformation pipeline
artifacts/model.pkl	Best trained ML model

## 📊 Model Evaluation
Multiple models were trained and evaluated using R² Score.

The best-performing model was selected and deployed for inference.

## 📜 Logging
Custom logging was implemented using Python’s logging module.
Logs are stored in the logs/ folder with timestamps.

## ✍️ Author
**Sanskar Jain**
📧 sanskarjain3112@gmail.com