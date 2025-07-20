import pandas as pd
import warnings
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score
import warnings
warnings.filterwarnings("ignore")

# Uyarıları bastır
warnings.filterwarnings("ignore")

# 🔹 Veriyi yükle
df_20 = pd.read_csv("20updated_file.csv")

# 🔹 Kullanılacak özellikler ve hedef
features = ['PTS', 'AST', 'TRB', 'FG%', 'MP']
target = 'MVP'

# 🔹 Eksik verileri ortalama ile doldur
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(df_20[features])

# 🔹 StandardScaler uygula
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

# 🔹 Yeni ölçeklenmiş DataFrame oluştur
scaled_df = pd.DataFrame(X_scaled, columns=features)
scaled_df['Player'] = df_20['Player']
scaled_df['Season'] = df_20['Season']
scaled_df['MVP'] = df_20['MVP']

# 🔹 Yeni CSV olarak kaydet (opsiyonel)
scaled_df.to_csv("scaled_20updated_file.csv", index=False)

# 🔹 Model giriş ve çıkışları
X_20 = scaled_df[features]
y_20 = scaled_df['MVP']

# 🔹 Eğitim-test bölmesi
X_train, X_test, y_train, y_test = train_test_split(X_20, y_20, test_size=0.2, random_state=42)

# 🔹 Kullanılacak modeller
models = {
    "Random Forest": RandomForestClassifier(random_state=42),
    "XGBoost": XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss'),
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42)
}

# 🔹 Model döngüsü
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"\n===== 🎓 {name} - Test Seti Doğruluğu (2004–2024): {accuracy:.4f} =====")
    print(f"\n===== {name} MVP Tahminleri (2004–2024) =====")

    correct_predictions = 0
    y_true_all = []
    y_pred_all = []

    for year in range(2004, 2025):
        year_data = scaled_df[scaled_df['Season'] == year].copy()
        
        if year_data.empty:
            print(f"{year} - Veri yok")
            continue

        X_year = year_data[features]
        probs = model.predict_proba(X_year)[:, 1]
        predicted_idx = probs.argmax()
        predicted_mvp = year_data.iloc[predicted_idx]['Player']
        
        actual_mvp_row = year_data[year_data['MVP'] == 1]
        if actual_mvp_row.empty:
            print(f"{year} - Gerçek MVP bilgisi yok")
            continue

        actual_mvp = actual_mvp_row['Player'].values[0]
        print(f"{year} - Tahmin: {predicted_mvp} | Gerçek: {actual_mvp}")

        if predicted_mvp == actual_mvp:
            correct_predictions += 1

        # Precision hesaplama için biriktir
        y_true = [1 if player == actual_mvp else 0 for player in year_data['Player']]
        y_pred = [1 if i == predicted_idx else 0 for i in range(len(year_data))]

        y_true_all.extend(y_true)
        y_pred_all.extend(y_pred)

    total_years = len(scaled_df['Season'].unique())
    precision = precision_score(y_true_all, y_pred_all, pos_label=1)

    print(f"\n🎯 {name} modeli {total_years} yılın {correct_predictions} tanesinde doğru tahmin yaptı.")
    print(f"✔️ Doğruluk oranı: {correct_predictions / total_years:.2%}")
    print(f"🎯 Precision (Pozitif sınıf - MVP=1): {precision:.4f}")
