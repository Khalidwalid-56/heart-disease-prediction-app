# Heart Disease Prediction App

This project focuses on predicting the presence of heart disease in patients using machine learning techniques. It is built using Python and integrates data preprocessing, model training, evaluation, and a user-friendly interface through Streamlit for real-time predictions.

## 💡 Objective
To develop a predictive model that helps in early detection of heart disease based on clinical parameters.

## 🧾 Dataset
The dataset includes several medical attributes such as:
- `age`: Age of the patient
- `sex`: Sex (1 = male; 0 = female)
- `cp`: Chest pain type
- `trestbps`: Resting blood pressure
- `chol`: Serum cholesterol
- `fbs`: Fasting blood sugar
- `restecg`: Resting electrocardiographic results
- `thalach`: Maximum heart rate achieved
- `exang`: Exercise-induced angina
- `oldpeak`: ST depression
- `slope`: Slope of the ST segment
- `ca`: Number of major vessels
- `thal`: Thalassemia

## ⚙️ Technologies Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- CatBoost, XGBoost, Random Forest, Linear Regression
- Streamlit (for UI)
- MLflow (for experiment tracking)

## 🧪 ML Workflow
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering and selection
- Training multiple ML models
- Evaluating model performance (accuracy, confusion matrix, etc.)
- Saving the best-performing model
- Creating an interactive Streamlit web app for prediction

## 📊 Models Used
- Logistic Regression
- Naive Bayes
- SVM
- KNN
- Decision Tree
- Random Forest
- XGBoost
- KMeans (Unsupervised)

## 📊 Streamlit UI
A simple and intuitive web interface allows users to input clinical data and receive predictions on heart disease risk instantly.

## Live Demo

🖥️ You can try the live app here: [Heart Disease Prediction App on Streamlit](https://your-app-name.streamlit.app)


## 📁 Project Structure
│── data/

│ ├── heart_disease.csv

│── notebooks/

│ ├── 01_data_preprocessing.ipynb

│ ├── 02_pca_analysis.ipynb

│ ├── 03_feature_selection.ipynb

│ ├── 04_supervised_learning.ipynb

│ ├── 05_unsupervised_learning.ipynb

│ ├── 06_hyperparameter_tuning.ipynb

│── models/

│ ├── final_model.pkl

│── ui/

│ ├── app.py (Streamlit UI)


## 🚀 How to Run the App
```bash
pip install -r requirements.txt
streamlit run ui_&_deployment/app.py
```

## 📌 Author
Mahmoud Bayoumi – Data Scientist

GitHub: [@MahmoudBayoumi](https://github.com/MahmoudBayoumi-AI)

[LinkedIn](https://www.linkedin.com/in/mahmoud-bayoumi-4a989b320/)
