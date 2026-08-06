from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("rain_prediction_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values from form
        MinTemp = float(request.form["MinTemp"])
        MaxTemp = float(request.form["MaxTemp"])
        Rainfall = float(request.form["Rainfall"])

        # Create DataFrame with feature names
        data = pd.DataFrame({
            "MinTemp": [MinTemp],
            "MaxTemp": [MaxTemp],
            "Rainfall": [Rainfall]
        })

        # Predict
        prediction = model.predict(data)

        # Display result
        if prediction[0] == 1:
            result = "☔ Rain Tomorrow"
        else:
            result = "☀️ No Rain Tomorrow"

        return render_template("index.html", prediction=result)

    except Exception as e:
        return render_template("index.html", prediction=f"Error: {e}")


if __name__ == "__main__":
    app.run(debug=True)