# Automobile Price Prediction (End-to-End ML Project)

## Project Overview

This project is an end-to-end machine learning application that predicts automobile prices using regression techniques. It follows an industry-standard pipeline including data preprocessing, multi-model comparison, hyperparameter tuning, and deployment using Streamlit.

---

## Objective

* Build multiple regression models
* Compare their performance using evaluation metrics
* Select the best model
* Optimize it using hyperparameter tuning
* Deploy the final model as a web application

---

## Dataset

* Automobile dataset
* Contains features such as:

  * Engine Size
  * Horsepower
  * Curb Weight
  * Mileage
  * Fuel Type
  * Body Style
* Target Variable: `price`

---

## Machine Learning Workflow

```text
Data Preprocessing → Model Comparison → Best Model Selection → Hyperparameter Tuning → Evaluation → Deployment
```

---

## Data Preprocessing

* Replaced missing values (`? → NaN`)
* Dropped null values
* Converted data types
* Encoded categorical features
* Applied feature scaling using StandardScaler

---

## Models Used

* Linear Regression
* Ridge Regression
* Lasso Regression
* Decision Tree Regressor
* Random Forest Regressor

---

## Model Selection Strategy

* Compared models using:

  * R² Score
  * RMSE
* Selected the best-performing model
* Applied GridSearchCV for hyperparameter tuning

---

## Results

* Random Forest performed best
* Achieved highest R² score and lowest RMSE
* Performance improved after tuning

---

## Deployment

* Built using Streamlit
* Provides a simple interface for user input
* Generates real-time predictions

---

## Project Structure

```bash
automobile-price-prediction/
│
├── data/
│   └── Automobile_data.csv
│
├── src/
│   ├── data_preprocessing.py
│   ├── pipeline.py
│   ├── model_training.py
│   ├── evaluation.py
│   ├── hyperparameter_tuning.py
│   ├── utils.py
│
├── artifacts/
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
```

---

## How to Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/your-username/automobile-price-prediction.git
cd automobile-price-prediction
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

```bash
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Train Model

```bash
python main.py
```

### 6. Run Application

```bash
streamlit run app.py
```

---

## Live Demo

Add your Streamlit deployment link here.

---

## Key Learnings

* Built a modular machine learning pipeline
* Implemented multi-model comparison
* Applied hyperparameter tuning
* Addressed feature consistency between training and inference
* Deployed a machine learning model using Streamlit

---

## Note

Model artifacts are not stored in the repository. They are generated during training and saved locally.

---

## Future Improvements

* Add complete feature input interface
* Deploy using a backend framework such as Flask
* Introduce model versioning
* Improve user interface

---

## Author

Veena Kutty

---

## Support

If you find this project useful, consider giving it a star on GitHub.
