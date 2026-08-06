from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("rain_prediction_model.pkl")


@app.route("/")
def home():
    return render_template("index.html", prediction=None)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values from form
        min_temp = float(request.form["MinTemp"])
        max_temp = float(request.form["MaxTemp"])
        rainfall = float(request.form["Rainfall"])
        humidity3pm = float(request.form["Humidity3pm"])
        pressure3pm = float(request.form["Pressure3pm"])
        windspeed3pm = float(request.form["WindSpeed3pm"])
        sunshine = float(request.form["Sunshine"])

        # Create feature array (same order as training)
        features = np.array([[
            min_temp,
            max_temp,
            rainfall,
            humidity3pm,
            pressure3pm,
            windspeed3pm,
            sunshine
        ]])

        # Predict
        prediction = model.predict(features)[0]

        if prediction == 1:
            result = "Rain Tomorrow 🌧️"
        else:
            result = "No Rain Tomorrow ☀️"

        return render_template(
            "index.html",
            prediction=result,
            min_temp=min_temp,
            max_temp=max_temp,
            rainfall=rainfall,
            humidity3pm=humidity3pm,
            pressure3pm=pressure3pm,
            windspeed3pm=windspeed3pm,
            sunshine=sunshine
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction=f"Error: {e}"
        )


if __name__ == "__main__":
    app.run(debug=True)