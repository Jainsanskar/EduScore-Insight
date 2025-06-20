from flask import Flask, request, render_template, redirect, url_for, session
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application
app.secret_key = 'your_secret_key'  # Required for session usage

## Route for home page
@app.route('/')
def index():
    prediction = session.pop('prediction', None)  # remove prediction after showing
    return render_template('index.html', results=prediction)

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')

    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),   # ✅ fixed
            writing_score=float(request.form.get('writing_score'))    # ✅ fixed
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        print("After Prediction")

        session['prediction'] = round(results[0], 2)  # store prediction temporarily
        return redirect(url_for('index'))  # PRG pattern: redirect after POST

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
