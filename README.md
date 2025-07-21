# 🎓 EduScore Insight: Predicting Student Performance

An end-to-end machine learning web application that predicts a student's **math score** based on demographic and academic features.  
This project demonstrates a complete ML pipeline — from data ingestion to real-time prediction using a Flask-based web interface.

---

## 📌 Problem Statement

Understanding the influence of socio-academic factors on student performance can help shape better educational policies and interventions.  
This application predicts a student’s `math score` using the following attributes:

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
2. **Data Ingestion** – Load the dataset and split into training and testing sets
3. **Data Transformation** – Handle missing values, encode categorical features, and scale numeric attributes using `Pipeline` & `ColumnTransformer`
4. **Model Training** – Train various models (Random Forest, XGBoost, CatBoost) with hyperparameter tuning
5. **Model Evaluation** – Evaluate and select the best model based on R² score
6. **Prediction Pipeline** – Develop a reusable pipeline for inference
7. **Web Deployment** – Deploy the model using Flask for live predictions

---

## 📁 Project Structure

```
EduScore-Insight/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   ├── utils.py
│   ├── logger.py
│   └── exception.py
│
├── artifacts/                  # Stores train/test splits, model, and preprocessor
├── templates/                  # HTML form for user input
├── app.py                      # Flask web application
├── logs/                       # Timestamped log files
├── requirements.txt
└── README.md
```

---

## 🧠 Technologies Used

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn**
- **CatBoost**, **XGBoost**
- **Flask**
- **HTML/CSS**
- **Pickle**

---

## 🧾 Artifacts

| File | Description |
|------|-------------|
| `artifacts/train.csv` | Training dataset |
| `artifacts/test.csv`  | Testing dataset  |
| `artifacts/preprocessor.pkl` | Serialized preprocessing pipeline |
| `artifacts/model.pkl` | Best trained ML model |

---

## 📊 Model Evaluation

- Multiple models were trained and evaluated using **R² Score**
- The best-performing model was serialized and used in the prediction pipeline

---

## 🪵 Logging

- Custom logging implemented using Python’s built-in `logging` module
- Logs stored under `logs/` with timestamps for traceability

---

## ✍️ Author

**Sanskar Jain**  
📧 sanskarjain3112@gmail.com
