💼 Salary Predictor App
A Machine Learning project that predicts employee salaries based on multiple factors like job title, experience, education, and location. Built using popular ensemble learning techniques such as Random Forest, Gradient Boosting, and Voting Classifiers to improve prediction accuracy.

📌 Project Objective
The objective of this project is to:

Analyze employee salary data.

Build and compare machine learning models.

Predict salaries using ensemble methods for higher accuracy.

Provide a simple Streamlit-based web interface for real-time predictions.

Dataset used: Kaggle - Salary Data

🧠 Machine Learning Techniques Used
Random Forest Regressor

Gradient Boosting Regressor

Voting Regressor (Combines multiple models for better results)

📂 Project Structure
bash
Copy
Edit
salary-predictor-app/
│
├── app.py                  # Streamlit app
├── model/
│   └── salary_model.pkl    # Trained ML model (saved using pickle)
├── data/
│   └── salary_dataset.csv  # Raw dataset used for training
├── utils.py                # Helper functions
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
🚀 How to Run the Project
Clone the repository:

bash
Copy
Edit
git clone https://github.com/SHRISHTI1414/salary-predictor-app.git
cd salary-predictor-app
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
🛠 Features
Input form for job title, experience, education level, and location.

Real-time salary prediction.

Simple and user-friendly interface using Streamlit.

Model built using ensemble methods for better performance.

📈 Model Performance
Trained on a real-world Kaggle dataset.

Models evaluated using metrics like R² Score and Mean Squared Error (MSE).

Voting Regressor combines the best of multiple models for robust predictions.

📚 Libraries Used
pandas, numpy – data handling

scikit-learn – ML models and preprocessing

streamlit – web interface

pickle – model serialization

📷 Sample Screenshot
(You can add a screenshot of the app interface here)

🙋‍♀️ Developed By
Shrishti Yadav
2nd Year Engineering Student, ABES Engineering College
Email: yshrishti39@gmail.com
GitHub: shrishti1414

📌 Note
This project is submitted as part of an academic assignment. The goal was to build an end-to-end machine learning pipeline including data preprocessing, model building, evaluation, and deployment using Streamlit.

