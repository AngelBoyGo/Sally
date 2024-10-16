# Sally - Heart Disease Risk Assessment Tool

Sally is a specialized heart disease risk assessment tool developed using the All of Us Research Program database. It's designed to help healthcare providers quickly assess a patient's risk of heart disease.

## Setup
1. Clone this repository
2. Install requirements: `pip install -r requirements.txt`
3. Run the Jupyter Notebook `model_training.ipynb` to train the model
4. Run the Flask app: `python app.py`
5. Open a web browser and go to `http://localhost:5000`

# Working with Concept IDs in the All of Us Database
The All of Us Research Program stores patient data using concept IDs, which are unique identifiers for medical metrics (e.g., blood pressure, BMI) or conditions (e.g., heart disease). If you're pulling data from this database:

Understand Concept IDs: Each health metric or condition has a specific concept ID.
Example:

3004249 = Diastolic Blood Pressure
316139 = Heart Disease
Writing Queries: Use SQL queries with these concept IDs to pull relevant data.
Example Query:

sql
Copy code
SELECT person_id, measurement_concept_id, value
FROM `your_workspace.measurement`
WHERE measurement_concept_id = 3004249
Navigating the Database:

Use the Google BigQuery console to explore the schema.
Reference the All of Us data dictionary for concept IDs to find more health metrics.
Quick Tip: When working with multiple IDs, use IN statements to grab data for multiple measurements at once:

sql
Copy code
WHERE measurement_concept_id IN (3004249, 3018586, 3043111)
This will help others easily navigate the database and extract the right data for their models without the struggle we went through.#

## Usage
1. Open the Sally web interface in your browser
2. Enter the patient's health metrics:
   - Age, gender, race, and ethnicity
   - Blood pressure (systolic and diastolic)
   - BMI
   - Cholesterol levels (total, HDL, LDL)
   - Glucose level
   - Waist circumference
   - Triglycerides
3. Click "Assess Risk" to get the prediction
4. Review the risk assessment and recommendations

## Customization
Sally is built on the All of Us database but can be adapted for other datasets. To use a different dataset:
1. Prepare your data in a similar format to the All of Us data
2. Modify the data loading and preprocessing steps in the Jupyter Notebook
3. Retrain the model with your data

## Troubleshooting
If you encounter any issues:
1. Ensure all dependencies are correctly installed
2. Check that the model file (.joblib) is in the correct directory
3. Verify that your input data is within expected ranges

## Contributing
We welcome contributions! Please see CONTRIBUTING.md for details on how to submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
- All of Us Research Program for the dataset




For any questions or support, please open an issue in this repository.
