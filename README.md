
# 💼 Customer Churn Prediction with Streamlit
This project is a machine learning web application built using Streamlit to predict customer churn — whether a customer will stay or leave a company. The prediction model is trained using a Random Forest Classifier based on customer attributes such as age, tenure, account balance, credit card ownership, and activity status.

## 📊 Features
- Binary classification: Churn (Exited = 1) or Not Churn (Exited = 0)
- Interactive web interface using Streamlit
- Predict based on user input fields (credit card, activity, salary, etc.)
- Model trained on real-world bank customer dataset
- Confusion matrix, accuracy, precision, recall, and F1-score evaluated

## 🧠 Machine Learning
- Model: Random Forest Classifier
- Evaluation Metrics:
* Accuracy: 86%
* Precision, Recall, F1-Score
- Dataset Features:
CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary
- Target Variable: Exited

## 🚀 How to Run Locally
1. **Clone the repository**
2. **Install requirements such as pandas, numpy, seaborn, matplotlib, sklearn, joblib, streamlit**
3. **Run the app**
streamlit run app.py
4. **(Optional) Explore the notebook**
   You can open churn_classification.ipynb in Jupyter Notebook to see how the model was built and trained.




