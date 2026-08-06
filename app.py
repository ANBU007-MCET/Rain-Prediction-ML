from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("rain_prediction_model.pkl")


@app.route('/')
def home():
    return render_template("index.html", prediction=None)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        min_temp = float(request.form['MinTemp'])
        max_temp = float(request.form['MaxTemp'])
        rainfall = float(request.form['Rainfall'])

        # Create input for model
        features = np.array([[min_temp, max_temp, rainfall]])

        # Predict
        prediction = model.predict(features)[0]

        # Convert prediction to text
        if prediction == 1:
            result = "Rain Tomorrow"
        else:
            result = "No Rain Tomorrow"

        return render_template(
            "index.html",
            prediction=result
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction=f"Error: {e}"
        )


if __name__ == "__main__":
    app.run(debug=True)