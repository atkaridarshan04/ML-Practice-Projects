# 📰 Fake News Detection using Machine Learning

This project builds a **Machine Learning Model** to detect fake news articles based on their **title and author**. Unlike other models that analyze the full text, this model relies on metadata to classify articles as **real/realiable (0) or fake/unreliable (1)**.

---

## 🚀 Project Overview

✅ **Machine Learning Model**  
- Algorithm: **Logistic Regression** (Binary Classification: Fake vs. Real News)
- Dataset Features: `id`, `title`, `author`, `text`, `label`
- **Important Note:** This model detects fake news based on **title & author** and does **not use the full text**.
- **Feature Engineering**: `TfidfVectorizer` applied to convert text into numerical form
- **Evaluation Metric**: Accuracy Score, Confusion Matrix

✅ **Key Steps in the Notebook**  
- Load and explore the dataset
- Apply **Stemming** to reduce words to their root form (e.g., "running" → "run")
- Preprocess text using **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert text into numerical form by measuring word importance
- Split the dataset into **training** and **testing** sets
- Train a **Logistic Regression** model
- Evaluate the model

---

## 📊 Dataset Overview
- **Dataset File:** Provided in the notebook
- **Columns:**
  - `id`: Unique article ID
  - `title`: **(Used for detection)** The headline of the news article
  - `author`: **(Used for detection)** The name of the author
  - `text`: Full article content (**Not used, could be incomplete**)
  - `label`: **1 → Fake news, 0 → Real news**

---

## 🧠 Model Training Steps

1. **Stemming**  
   - Reduces words to their root form to standardize text (e.g., "playing" → "play"). This helps in reducing dimensionality and improving model performance.

2. **TF-IDF (Term Frequency-Inverse Document Frequency)**  
   - Converts text data into numerical form by assigning importance scores to words. Frequently used words across documents get lower importance, while unique words in a document get higher importance.

3. **Model Selection: Logistic Regression**  
   - Train a **Logistic Regression classifier** for binary classification

4. **Evaluation**  
   - Measure model performance using **accuracy score**

---

## 🎯 Results
- **Achieved Accuracy:** `98.63` on training data and `97.90` on test data
- **Confusion Matrix:** 

        [[2004, 73]]
        [[14, 2069]]

---