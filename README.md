 Salary Predictor App
====================

A machine learning web application that predicts employee salaries based on multiple features such as job title, experience, education level, and location. The project utilizes ensemble techniques like Random Forest, Gradient Boosting, and Voting Regressors to improve predictive accuracy. A clean and interactive GUI is built using Streamlit for real-time prediction and is deployed on Streamlit Cloud.

 

Project Objective
-----------------

The objective of this project is to:

- Analyze employee salary data
- Build and compare machine learning models
- Predict salaries using ensemble methods for better accuracy
- Provide a Streamlit-based web interface for easy access

 Dataset Used : Kaggle – Employee Salary Dataset

---

Machine Learning Techniques Used
--------------------------------

- Random Forest Regressor
- Gradient Boosting Regressor (XGBoost)
- Voting Regressor (combines top models for better accuracy)

---

Project Structure
-----------------

salary-predictor-app/
│
├── app.py                  # Streamlit app
├── model/
│   └── salary_model.pkl    # Trained ML model (Pickle)
├── data/
│   └── salary_dataset.csv  # Dataset used for training
├── utils.py                # Helper functions
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

 

How to Run the Project
----------------------

 1. Clone the Repository

git clone https://github.com/SHRISHTI1414/salary-predictor-app.git
cd salary-predictor-app

 
2. Install the Dependencies

pip install -r requirements.txt

3. Launch the Streamlit App

streamlit run app.py

 
Features
--------

- Interactive form to input job title, experience, education level, and location
- Real-time salary prediction based on user input
- Streamlit-based GUI for ease of use
- Uses ensemble models to ensure higher accuracy

---

Model Performance
-----------------

- Trained on a real-world dataset from Kaggle
- Performance evaluated using R² Score and RMSE
- Voting Regressor provided the best results by combining Random Forest and XGBoost
- Confirmed model performance through IBM AutoAI

---

Libraries Used
--------------

- `pandas`, `numpy` – Data manipulation and analysis
- `scikit-learn` – Model training and evaluation
- `xgboost`, `lightgbm` – Gradient boosting models
- `pickle` – Model serialization
- `streamlit` – GUI development



Author
------

**Shrishti Yadav**  
2nd Year B.Tech CSE  
ABES Engineering College, Ghaziabad  
Email: yshrishti39@gmail.com  
GitHub: [shrishti1414](https://github.com/SHRISHTI1414)
