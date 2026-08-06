# 🌧️ Rain Prediction System using Machine Learning

A Machine Learning-based Rain Prediction System developed using **Python**, **Flask**, and **Logistic Regression**. This web application predicts whether it will rain based on seven important weather parameters.

## 🌐 Live Demo

🔗 https://rain-prediction-ml-1.onrender.com

---

# 📌 Project Overview

This project predicts the possibility of rainfall using a Machine Learning model trained on historical weather data. Users can enter weather conditions through an interactive web interface and receive an instant prediction.

---

# ✨ Features

- 🌧️ Rain prediction using Machine Learning
- 🤖 Logistic Regression algorithm
- 📊 Trained with 7 weather features
- 🖥️ User-friendly Flask web application
- ⚡ Instant prediction results
- 📱 Responsive interface
- ☁️ Deployed on Render

---

# 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Git
- GitHub
- Render

---

# 📂 Dataset

**Dataset:** archive.csv

### Features Used

- Minimum Temperature (°C)
- Maximum Temperature (°C)
- Rainfall (mm)
- Humidity at 3 PM (%)
- Wind Speed at 3 PM (km/h)
- Pressure at 3 PM (hPa)
- Sunshine (hours)

### Target

- Rain Tomorrow (Yes / No)

---

# 🤖 Machine Learning Model

**Algorithm:** Logistic Regression

**Model Accuracy:** **79%**

---

# 📷 Application Screenshots

## 🏠 Home Page

![Home Page](screenshots/home.png.png)

## 🌧️ Prediction Result

![Prediction Result](screenshots/prediction.png.png)

---

# 🧪 Example Test Input

| Feature | Value |
|----------|------:|
| Minimum Temperature | 18.5 |
| Maximum Temperature | 28.4 |
| Rainfall | 12.6 |
| Humidity (3 PM) | 83 |
| Wind Speed (3 PM) | 22 |
| Pressure (3 PM) | 1008.4 |
| Sunshine | 2.8 |

### Prediction

```
Rain Tomorrow
```

---

# 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/ANBU007-MCET/Rain-Prediction-ML.git
```

### Move into the Project Folder

```bash
cd Rain-Prediction-ML
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```
http://127.0.0.1:5000
```

---

# 📁 Project Structure

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
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── screenshots/
    ├── home.png.png
    └── prediction.png.png
```

---

# 🎯 Future Enhancements

- Improve prediction accuracy
- Add weather API integration
- Show prediction probability
- Display weather charts
- Support multiple cities
- Mobile-friendly enhancements

---

# 👨‍💻 Developer

**Anbu Selvan K**

**B.E. Artificial Intelligence & Data Science**

Dr. Mahalingam College of Engineering and Technology

GitHub:
https://github.com/ANBU007-MCET

---

# 🌐 Live Application

https://rain-prediction-ml-1.onrender.com

---

# ⭐ Support

If you found this project helpful, please give it a ⭐ on GitHub.

---

# 📄 License

This project is developed for educational and academic purposes.
