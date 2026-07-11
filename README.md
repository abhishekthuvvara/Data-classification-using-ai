# 🌸 AI Project 2 - Data Classification Using K-Nearest Neighbors (KNN)

## 📌 Project Overview

This project is part of the **Artificial Intelligence Internship Program** by **DecodeLabs**.

The objective is to build a **Machine Learning Classification Model** using the famous **Iris Dataset**. The project demonstrates the complete supervised learning workflow including data preprocessing, model training, prediction, evaluation, visualization, and model saving.

---

## 🎯 Project Goal

Develop a classification model that can accurately predict the species of an Iris flower based on its measurements.

The project covers:

- Loading and exploring a dataset
- Data preprocessing
- Feature scaling
- Splitting data into training and testing sets
- Training a KNN classifier
- Making predictions
- Evaluating model performance
- Saving the trained model
- Predicting new flower samples

---

## 📂 Dataset

**Dataset Used:** Iris Dataset (Built into Scikit-Learn)

The dataset contains:

- **150 Flower Samples**
- **4 Input Features**
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- **3 Target Classes**
  - Setosa
  - Versicolor
  - Virginica

---

## 🛠 Technologies Used

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib

---

## 📁 Project Structure

```
AI_Project2_Data_Classification/
│
├── main.py
├── README.md
├── requirements.txt
├── iris_model.pkl
│
├── output/
│   ├── pairplot.png
│   ├── class_distribution.png
│   ├── confusion_matrix.png
│   └── accuracy_vs_k.png
│
└── screenshots/
```

---

## ⚙ Features

✅ Load Iris Dataset

✅ Data Exploration

✅ Data Visualization

✅ Feature Scaling using StandardScaler

✅ Train-Test Split

✅ K-Nearest Neighbors (KNN) Classification

✅ Model Prediction

✅ Accuracy Evaluation

✅ Confusion Matrix

✅ Classification Report

✅ Best K Value Selection

✅ Save Trained Model

✅ Predict Custom Flower Species

---

## 🚀 Installation

Clone the repository

```bash
Git clone https://github.com/abhishekthuvvara/Data-classification-using-ai.git
```

Move into the project folder

```bash
cd AI_Project2_Data_Classification
```

Install required libraries

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Project

```bash
python main.py
```

---

## 📊 Output

The project generates:

- Dataset Information
- Statistical Summary
- Model Accuracy
- Confusion Matrix
- Classification Report
- Pair Plot
- Class Distribution Graph
- Accuracy vs K Graph
- Saved Machine Learning Model

---

## 📈 Machine Learning Workflow

```
Load Dataset
      │
      ▼
Explore Dataset
      │
      ▼
Preprocess Data
      │
      ▼
Feature Scaling
      │
      ▼
Train-Test Split
      │
      ▼
Train KNN Model
      │
      ▼
Prediction
      │
      ▼
Model Evaluation
      │
      ▼
Visualization
      │
      ▼
Save Model
```

---

## 📷 Sample Outputs

### Pair Plot

!![alt text](<Screenshot 2026-07-11 110953-1.png>)

---

### Confusion Matrix

![alt text](<Screenshot 2026-07-11 111311.png>)

---

### Accuracy vs K
![alt text](<Screenshot 2026-07-11 111415.png>)
---

## 📚 Concepts Learned

- Supervised Learning
- Classification
- K-Nearest Neighbors (KNN)
- Data Preprocessing
- Feature Scaling
- Train-Test Split
- Model Training
- Model Evaluation
- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Data Visualization
- Model Persistence

---

## 🔮 Future Improvements

- Hyperparameter Tuning
- Cross Validation
- GridSearchCV
- Interactive GUI
- Streamlit Web Application
- Flask API Deployment
- Docker Support
- Model Comparison with Other Algorithms

---

## 👨‍💻 Author

**Abhishek Tuvvara**

B.Tech Artificial Intelligence Student

GitHub: https://github.com/abhishekthuvvara

LinkedIn:https://www.linkedin.com/in/thuvvara-abhishek-01768b362/

---

## 📜 License

This project is created for educational and internship purposes under the DecodeLabs AI Internship Program.