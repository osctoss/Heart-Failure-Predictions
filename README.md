# ❤️ CardioPredict: AI-Powered Heart Failure Prediction 🧬

**Project Type:** Machine Learning, Health Analytics
**Tech Stack:** Python, Flask, Scikit-learn, Pandas, HTML/CSS, GitHub

---

## 🚀 Project Overview

CardioPredict is a **web-based application** designed to **predict the likelihood of mortality due to heart failure** based on a patient's clinical records. It uses a machine learning model trained on the "Heart Failure Clinical Records" dataset from Kaggle.

The model is deployed using the **Flask** framework and provides a clean, interactive UI for real-time prediction.

> Built as part of the **DevTown Predictive Modelling Bootcamp**.

---

## ✨ Features

* **🖥️ Interactive UI** – Clean, intuitive form for inputting patient clinical data
* **⚡ Real-Time Predictions** – Instantly shows whether a patient is at risk
* **📱 Responsive Design** – Works seamlessly across all devices
* **🔁 Scalable Backend** – Powered by Flask for easy integration and updates

---

## 🧠 Technologies Used

**Backend:** Python, Flask
**Machine Learning:** Scikit-learn, Pandas, NumPy
**Frontend:** HTML, CSS
**Deployment:** Git & GitHub

---

## 📁 Project Structure

```
Heart_Failure/
│
├── .venv/                         # Virtual environment files
├── static/
│   └── style.css                 # Styling for the UI
├── templates/
│   └── index.html               # Frontend HTML file
├── app.py                        # Main Flask backend
├── model.pkl                     # Trained ML model
├── Heart_Failure_Prediction.ipynb  # Notebook for training & analysis
├── README.md                     # You're reading it!
└── requirements.txt              # Project dependencies
```

---

## ⚙️ Setup and Installation

### 🔄 Step 1: Clone the Repository

```bash
git clone https://github.com/osctoss/Heart-Failure-Prediction.git
cd Heart-Failure-Prediction
```

### 🧪 Step 2: Create a Virtual Environment

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 📦 Step 3: Install Dependencies

Make sure your `requirements.txt` contains:

```
Flask
pandas
numpy
scikit-learn
pickle
```

Then run:

```bash
pip install -r requirements.txt
```

### ▶️ Step 4: Run the Application

```bash
flask run
```

The app will be available at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💻 How to Use

1. Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)
2. You’ll see a form with **12 input fields** for clinical data
3. Fill in the patient’s details accurately
4. Click on **“Analyze & Predict”**
5. The model will display whether the patient is **likely to survive or not**

---

## 📊 Model Details & Performance

The model used is a **Logistic Regression** classifier trained on the Kaggle Heart Failure dataset.

### 🔧 Preprocessing:

* Standardized numeric features using `StandardScaler`

### 🏋️‍♂️ Training:

* Trained on **80%** of data, tested on **20%**

### 📈 Performance:

* Achieved **82% accuracy** on test data

> For full training and evaluation workflow, refer to: `Heart_Failure_Prediction.ipynb`

---

## 👤 Author

**Manish Patel (aka Osctoss)**
📫 [osctoss.net@gmail.com](mailto:osctoss.net@gmail.com)
🌐 [GitHub](https://github.com/osctoss)

---
