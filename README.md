# 🚗 Automobile Price Prediction using Regression Models

## 📌 Project Overview

This project focuses on predicting **automobile prices** using multiple regression algorithms and identifying the **best-performing model** based on evaluation metrics.

We implemented a **modular machine learning pipeline** including data preprocessing, model training, and evaluation.

---

## 🎯 Objective

* Build multiple regression models
* Compare their performance
* Select the best model based on:

  * R² Score
  * RMSE (Root Mean Squared Error)

---

## 📊 Dataset

* **Dataset Name:** Automobile Dataset
* Contains features like:

  * Engine size
  * Horsepower
  * Fuel type
  * Body style
  * Mileage
* **Target Variable:** `price`

---

## 🧹 Data Preprocessing

* Handled missing values (`? → NaN`)
* Dropped null values
* Converted data types
* Encoded categorical features using **Label Encoding**
* Applied **Feature Scaling** for linear models

---

## ⚙️ Models Used

* Linear Regression
* Ridge Regression
* Lasso Regression
* Decision Tree Regressor
* Random Forest Regressor

---

## 📈 Model Evaluation Metrics

* **R² Score** → Measures accuracy
* **RMSE** → Measures prediction error

---

## 🏆 Results

| Model           | R² Score | RMSE     |
| --------------- | -------- | -------- |
| Random Forest ⭐ | Highest  | Lowest   |
| Decision Tree   | Good     | Moderate |
| Linear Models   | Average  | Higher   |

👉 **Random Forest performed the best** due to its ability to handle non-linear relationships and reduce overfitting.

---

## 🧠 Key Insights

* Linear models struggle with complex data
* Tree-based models capture non-linearity better
* Ensemble methods (Random Forest) give the most accurate predictions

---

## 📁 Project Structure

```
project/
│
├── data/
│   └── Automobile_data.csv
│
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── evaluation.py
│
├── main.py
├── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Project

```bash
python main.py
```

---

## 📦 Requirements

* Python 3.x
* pandas
* numpy
* scikit-learn
* matplotlib

---

## 🔮 Future Improvements

* Hyperparameter tuning (GridSearchCV)
* Feature importance visualization
* Model deployment (Streamlit / Flask)
* Pipeline automation

---

## 👩‍💻 Author

**Veena Kutty**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
