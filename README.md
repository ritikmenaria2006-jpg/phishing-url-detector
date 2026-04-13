# phishing-url-detector
# Phishing URL Detector (Machine Learning Project)

A **Machine Learning-based web application** that detects whether a given URL is **phishing (malicious)** or **legitimate (safe)** using feature extraction and classification techniques.

---

## 🚀 Project Overview

Phishing attacks are one of the most common cybersecurity threats. This project aims to identify suspicious URLs by analyzing their structure and predicting whether they are harmful.

The system uses a **Random Forest Machine Learning model** trained on URL-based features and provides results through a simple web interface.

---

## ✨ Features

* 🔍 Detect phishing vs legitimate URLs
* ⚡ Fast prediction using trained ML model
* 🌐 Simple and interactive web interface (Flask)
* 🧠 Feature extraction from URLs
* 📊 Lightweight and easy to run

---

## 🛠️ Tech Stack

* **Python**
* **Flask** (Web Framework)
* **Scikit-learn** (Machine Learning)
* **Pandas** (Data Handling)

---

## 📂 Project Structure

```
phishing-url-detector/
│
├── dataset/
│   └── phishing.csv        # Sample dataset
│
├── model/
│   └── model.pkl          # Trained model (generated after training)
│
├── feature_extraction.py  # Extracts features from URLs
├── train_model.py         # Trains ML model
├── app.py                 # Flask web application
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## ⚙️ How It Works

1. User inputs a URL in the web app
2. System extracts features such as:

   * URL length
   * HTTPS usage
   * Number of dots
   * Presence of special characters (@, -)
   * Suspicious keywords (login, verify, bank, etc.)
3. The trained ML model predicts:

   * ⚠️ **Phishing URL**
   * ✅ **Safe URL**

---

## 🧠 Machine Learning Model

* Algorithm: **Random Forest Classifier**
* Input: Extracted features from URLs
* Output: Binary classification (Phishing / Safe)

---

## ▶️ How to Run This Project

### 🔹 Step 1: Download the Project

* Download ZIP or clone repository

```
git clone https://github.com/YOUR_USERNAME/phishing-url-detector.git
cd phishing-url-detector
```

---

### 🔹 Step 2: Install Dependencies

Make sure Python is installed, then run:

```
pip install -r requirements.txt
```

---

### 🔹 Step 3: Train the Model

Run the following command:

```
python train_model.py
```

✅ This will:

* Train the ML model
* Save it as `model/model.pkl`

---

### 🔹 Step 4: Run the Web Application

```
python app.py
```

---

### 🔹 Step 5: Open in Browser

Go to:

```
http://127.0.0.1:5000/
```

Enter a URL and check if it's phishing or safe.

---

## 📊 Example

| Input URL                      | Prediction  |
| ------------------------------ | ----------- |
| http://secure-login-paypal.com | ⚠️ Phishing |
| https://google.com             | ✅ Safe      |

---

## ⚠️ Important Notes

* `model.pkl` is generated after training (not included initially)
* The dataset provided is small (for demo purposes)
* For better accuracy, use a large real-world dataset

---

## 🚀 Future Improvements

* Use large-scale phishing datasets (10,000+ URLs)
* Improve accuracy using advanced ML models
* Deploy as a live web application
* Create browser extension (Chrome)
* Add REST API support

---

## 👨‍💻 Author

Your Name

---

## ⭐ Support

If you found this project helpful:

* ⭐ Star this repository
* 🍴 Fork it
* 📢 Share it

---

## 📌 Keywords

`machine learning` `cybersecurity` `phishing detection` `python` `flask` `url classifier`
