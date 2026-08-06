# 🌧️ Rain Prediction System using Machine Learning

A Machine Learning-based Rain Prediction System developed using **Python**, **Flask**, and **Logistic Regression**. This web application predicts whether it will rain based on seven weather parameters entered by the user.

🔗 **Live Demo:** https://rain-prediction-ml-1.onrender.com

---

## 📌 Project Overview

This project uses a Logistic Regression model trained on historical weather data to predict the possibility of rainfall. Users can enter weather conditions through a simple web interface and receive an instant prediction.

---

## ✨ Features

- 🌧️ Predicts whether it will rain or not
- 🤖 Machine Learning model using Logistic Regression
- 🖥️ Simple and user-friendly Flask web interface
- 📊 Trained using 7 important weather features
- ⚡ Instant prediction results
- 🌐 Deployed on Render
- 📱 Responsive and clean UI

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- Joblib
- Git & GitHub
- Render

---

## 📂 Dataset

Dataset: Weather Rain Prediction Dataset (`archive.csv`)

### Features Used

- Minimum Temperature (°C)
- Maximum Temperature (°C)
- Rainfall (mm)
- Humidity at 3 PM (%)
- Wind Speed at 3 PM (km/h)
- Pressure at 3 PM (hPa)
- Sunshine (hours)

Target:

- Rain Tomorrow (Yes / No)

---

## 📈 Machine Learning Model

Algorithm:

- Logistic Regression

Model Accuracy:

**79%**

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/ANBU007-MCET/Rain-Prediction-ML.git
```

Go to project folder

```bash
cd Rain-Prediction-ML
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📷 Application Screenshots

### Home Page

![Home Page](screenshots/home.png)

### Prediction Result

![Prediction Result](screenshots/prediction.png)

---

## 🧪 Example Test Input

| Feature | Value |
|----------|------:|
| Minimum Temperature | 18.5 |
| Maximum Temperature | 28.4 |
| Rainfall | 12.6 |
| Humidity (3 PM) | 83 |
| Wind Speed (3 PM) | 22 |
| Pressure (3 PM) | 1008.4 |
| Sunshine | 2.8 |

Expected Prediction:

```
Rain Tomorrow
```

---

## 📁 Project Structure

```
Rain-Prediction-ML
│
├── app.py
├── requirements.txt
├── rain_prediction_model.pkl
├── archive.csv
├── Model_Training.ipynb
├── README.md
│
├── templates
│   └── index.html
│
├── static
│   └── style.css
│
└── screenshots
    ├── home.png
    └── prediction.png
```

---

## 🎯 Future Improvements

- Improve prediction accuracy
- Add weather API integration
- Display prediction probability
- Include rainfall visualization charts
- Deploy with Docker
- Add user authentication

---

## 👨‍💻 Developer

**Anbu Selvan K**

Bachelor of Engineering (Artificial Intelligence & Data Science)

Dr. Mahalingam College of Engineering and Technology

GitHub:
https://github.com/ANBU007-MCET

---

## 🌐 Live Demo

https://rain-prediction-ml-1.onrender.com

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is developed for educational and academic purposes.
