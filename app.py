from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)
app.template_folder = os.path.abspath('templates')

# Load the trained model
model = joblib.load('heart_disease_model.joblib')

# Print model features for debugging
print("Model features:", model.feature_names_in_)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Define the expected feature order
        feature_order = [
            'gender_concept_id', 'race_concept_id', 'ethnicity_concept_id', 'age',
            'diastolic_bp', 'hdl_cholesterol', 'cholesterol', 'systolic_bp', 'glucose',
            'bmi', 'total_cholesterol', 'ldl_cholesterol', 'waist_circumference',
            'triglycerides', 'condition_316139', 'condition_316866', 'condition_320128',
            'condition_321318', 'condition_442604', 'condition_4108356',
            'condition_4108357', 'condition_4108358', 'condition_4185932', 'condition_4329847'
        ]

        # Create a dictionary to store user inputs
        user_inputs = {}
        for feature in feature_order:
            if feature.startswith('condition_'):
                user_inputs[feature] = 0  # Set conditions to 0 by default
            else:
                user_inputs[feature] = float(request.form.get(feature, 0))

        # Create DataFrame with correct feature order
        input_df = pd.DataFrame([user_inputs])

        # Print input DataFrame for debugging
        print("Input DataFrame:")
        print(input_df)

        print("Input DataFrame shape:", input_df.shape)
        print("Input DataFrame columns:", input_df.columns)
        print("First row of input data:", input_df.iloc[0])

        # Make prediction
        probabilities = model.predict_proba(input_df)
        if probabilities.shape[1] > 1:
            probability = probabilities[0][1]
        else:
            probability = probabilities[0][0]

        # Determine risk level
        if probability < 0.3:
            risk_level = "Low Risk"
            risk_class = "low-risk"
        elif probability < 0.6:
            risk_level = "Moderate Risk"
            risk_class = "moderate-risk"
        else:
            risk_level = "High Risk"
            risk_class = "high-risk"

        # Return the rendered template with results
        return render_template(
            'results.html', 
            risk_level=risk_level,
            risk_class=risk_class,
            probability=f"{probability:.2%}",
            user_inputs=user_inputs
        )

if __name__ == '__main__':
    print("Current working directory:", os.getcwd())
    print("Contents of current directory:", os.listdir())
    print("Contents of templates directory:", os.listdir('templates'))
    app.run(debug=True)
