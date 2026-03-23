# Symptom-to-Disease-Chatbot
The dataset used in the Symptom-to-Disease Chatbot project consists of structured medical records where each entry represents a disease along with its associated symptoms. The primary objective of this data is to map combinations of symptoms to a specific disease, enabling machine learning models to learn patterns for accurate prediction.

## 📁 Dataset Structure
Disease Column : Contains the name of the disease (target variable).
Symptom Columns (Symptom_0 to Symptom_16) : Each column represents a possible symptom, A single row may contain multiple symptoms distributed across these columns.

## Data Preprocessing

To make the dataset usable for machine learning:

Combine Symptoms
All symptom columns are merged into a single list per row
Example:
["fever", "headache", "fatigue"]

Clean Data

Remove empty values ("", "None")

Standardize symptom names

Feature Encoding

Use MultiLabelBinarizer to convert symptoms into binary features

Each symptom becomes a column with:

1 → symptom present

0 → symptom absent

Label Encoding

Convert disease names into numeric labels for model training

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

## 🧠 How It Works

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




# 🎯 Key Features
Symptom preprocessing and cleaning
Multi-label feature encoding
Machine learning model training (Random Forest)
Model evaluation (accuracy & cross-validation)
Confusion matrix visualization
Top-N disease prediction with confidence


#💡 Objective
To build an intelligent system that can assist users in identifying potential diseases based on symptoms, improving early awareness and supporting healthcare decision-making.





## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

