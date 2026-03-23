# Symptom-to-Disease-Chatbot
The dataset used in the Symptom-to-Disease Chatbot project consists of structured medical records where each entry represents a disease along with its associated symptoms. The primary objective of this data is to map combinations of symptoms to a specific disease, enabling machine learning models to learn patterns for accurate prediction.

## 📁 Dataset Structure
Disease Column : Contains the name of the disease (target variable).
Symptom Columns (Symptom_0 to Symptom_16) : Each column represents a possible symptom, A single row may contain multiple symptoms distributed across these columns.

## Data Preprocessing

1) To make the dataset usable for machine learning:
2) Combine Symptoms
3) All symptom columns are merged into a single list per row
Example:
["fever", "headache", "fatigue"]
4) Clean Data
5) Remove empty values ("", "None")
6) Standardize symptom names
7) Feature Encoding
------Use MultiLabelBinarizer to convert symptoms into binary features
8) Each symptom becomes a column with  :
     1 → symptom present
     0 → symptom absent
9) Label Encoding :  Convert disease names into numeric labels for model training

## 📊 Exploratory Data Analysis

- Distribution of diseases in dataset  
- Frequency of symptoms  
- Most common symptoms across diseases  
- Correlation between symptoms

## 📈 Model Performance

- Accuracy Score  
- Cross-validation score  
- Precision & Recall  
- F1-score  
- Confusion Matrix analysis

## 🧪 Model Comparison

The following models were tested:

- Decision Tree  
- Random Forest (Best Performing)  
- Naive Bayes  
- K-Nearest Neighbors (KNN)  

Random Forest achieved the highest accuracy and stability.

## 📊 Model Performance

The following machine learning models were trained and evaluated on the dataset:

| Model              | Accuracy |
|-------------------|----------|
| Decision Tree     | 0.6667   |
| Random Forest     | 0.8889   |
| Naive Bayes       | 1.0000   |
| K-Nearest Neighbors (KNN) | 1.0000 |

> ⚠️ Note: Extremely high accuracy (1.0) may indicate overfitting due to dataset size or feature simplicity.

---

## 📈 Evaluation Details

- Dataset size: 313 samples  
- Number of features: 152  
- Cross-validation used for reliable evaluation  
- Confusion Matrix used for visualization  

---

## 🧠 Insights

- Random Forest provides a balanced and reliable performance  
- Naive Bayes and KNN achieved perfect accuracy but may overfit  
- Decision Tree performs lower compared to ensemble methods  

---

##  How It Works

1. User enters symptoms  
2. Symptoms are cleaned and formatted  
3. Converted into binary feature vector  
4. Model predicts disease probabilities  
5. Top 3 diseases are displayed with confidence scores

## 💬 Chatbot Features

- Accepts user symptoms as input  
- Predicts diseases instantly  
- Shows top predictions  
- Displays confidence percentage  
- Provides description and precautions

## 🧾 Technologies Used

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Matplotlib / Seaborn

## 🧪 Example

Input:
fever, headache, fatigue  

Output:
Flu (92%)  
Common Cold (5%)  
Malaria (3%)  

## 🏆 Achievements

- Built end-to-end ML pipeline  
- Developed interactive chatbot  
- Achieved high accuracy using Random Forest  



## 🌟 Overview

An intelligent chatbot that predicts diseases based on user symptoms using a trained **Random Forest model**.  
It provides **top predictions with confidence scores** and helps users understand possible health conditions.

---

## 🎯 Features

✨ Symptom-based disease prediction  
✨ Top 3 predictions with probability  
✨ Interactive chatbot UI (Streamlit)  
✨ Clean and fast ML pipeline  
✨ Real-time predictions  

    project/
    │── app.py
    │── train_model.py
    │── requirements.txt
    │── README.md
    │── models/
    │   ├── disease_model.pkl
    │   ├── mlb.pkl
    │   ├── label_encoder.pkl




## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

