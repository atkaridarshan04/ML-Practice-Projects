# 📩 Email Classification using Machine Learning

This project builds a **Machine Learning Model** to classify emails using **Logistic Regression**. The dataset consists of email text, and the model predicts whether an email is spam or not.

---

## 🚀 Project Overview

✅ **Machine Learning Model**  
- Algorithm: **Logistic Regression** (Binary Classification: Spam vs. Non-Spam)
- Dataset: `mail_data.csv`
- **Feature Engineering**: Text data is converted into numerical form using `TfidfVectorizer`
- **Evaluation Metric**: Accuracy Score

✅ **Key Steps in the Notebook**  
- Load and explore the dataset
- Check for missing values and dataset shape
- Preprocess text using **TF-IDF (Term Frequency-Inverse Document Frequency)**
- Split the dataset into **training** and **testing** sets
- Train a **Logistic Regression** model
- Evaluate the model using accuracy score

---

## 📊 Dataset Overview
- **Dataset File:** `mail_data.csv`
- **Columns:**
  - `category`: Spam or Ham
  - `message`: The email content

---

## 🧠 Model Training Steps

1. **Data Preprocessing**  
   - Convert text to lowercase and remove special characters
   - Apply **TF-IDF Vectorization** to transform text into numerical data

2. **Model Selection: Logistic Regression**  
   - Train a **Logistic Regression classifier** for binary classification

3. **Evaluation**  
   - Measure model performance using **accuracy score**

---

## 🎯 Results
- **Achieved Accuracy:** `95.24` on test data and  `96.70` on train data.
- **Confusion Matrix:**

        [[960, 0]]  
        [[53, 102]]

---
