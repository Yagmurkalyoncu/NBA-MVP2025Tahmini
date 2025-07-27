# 🏀 NBA 2025 MVP Prediction – A Machine Learning Project

This project uses NBA player statistics to predict the **Most Valuable Player (MVP)** of the **2025 season** using machine learning algorithms.

---

## 👥 Authors

**Yağmur Kalyoncu**  
Department of Computer Engineering  
Ankara University – Ankara, Turkey  
📧 kalyoncuyagmur67@gmail.com  

**Halime Şahnur Çöğür**  
Department of Computer Engineering  
Ankara University – Ankara, Turkey  
📧 sahnurcogur98@gmail.com  

---

## 📌 Abstract

In this project, player performance data from NBA seasons between **2004 and 2024** is used to predict the **2025 MVP**.  
Three different machine learning algorithms were implemented and compared:

- **Random Forest Classifier**
- **XGBoost Classifier**
- **Logistic Regression**

The model performances were evaluated using **precision** as the primary metric, and the best-performing model was used to generate MVP candidate predictions for the 2025 season.

---

## 🔍 Features Used

The following statistical features were used for prediction:

- `PTS` — Points per game  
- `AST` — Assists per game  
- `TRB` — Rebounds per game  
- `FG%` — Field Goal Percentage  
- `MP` — Minutes per game  

Target:  
- `MVP` — 1 if the player was MVP, 0 otherwise

---

## 🧠 Methodology

### 1. Data Collection
Player statistics were collected from [Basketball-Reference.com](https://www.basketball-reference.com) for each season between 2004–2024 using web scraping techniques. Each player was labeled with a binary `MVP` tag (1 for MVP, 0 otherwise).

### 2. Data Preprocessing
- Missing values were filled using **mean imputation** via `SimpleImputer`.
- Features were **standardized** using `StandardScaler`.
- Data was split into features (`X`) and target (`y`) for training.

### 3. Modeling
Three machine learning models were trained and compared:

- ✅ **Random Forest** – Showed the best performance due to its ability to model complex relationships.
- ✅ **XGBoost** – A powerful boosting algorithm, effective on imbalanced classification tasks.
- ❌ **Logistic Regression** – Simple and interpretable but had limited predictive power for this problem.

📌 The **precision score** was chosen as the evaluation metric to prioritize minimizing false positives (predicting a non-MVP as MVP).

### 4. 2025 MVP Prediction
The best-performing model (Random Forest) was used to make predictions for the 2025 season. It calculated MVP probabilities for all players and returned the **Top 5 candidates** based on predicted probability scores.

---

## 📈 Results

- **Random Forest** achieved the highest precision score.
- **XGBoost** also performed well, especially on 10-year data.
- **Logistic Regression** struggled with the complexity of MVP prediction due to its linear nature.

### 📊 Key Analysis
- MVPs usually have higher `PTS`, `MP`, and `FG%` values than non-MVPs.
- Age is not a strong predictor; performance metrics are more critical.
- Adding more historical data (20 years) does not always improve model accuracy.

---

## 🔮 Sample Prediction Output

```text
🎯🎯 2025 Most Valuable Player (MVP) Prediction – Random Forest

1. Nikola Jokic              (Probability: 0.5500)
2. Shai Gilgeous Alexander   (Probability: 0.2900)
3. Giannis Antetokounmpo     (Probability: 0.2200)
4. Domantas Sabonis          (Probability: 0.1900)
5. Luka Dončić               (Probability: 0.1300)

