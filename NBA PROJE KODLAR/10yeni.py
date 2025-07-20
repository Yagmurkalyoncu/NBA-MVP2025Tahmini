import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score
import warnings
warnings.filterwarnings("ignore")

# Veriyi yükledik ve okuduk
df_10 = pd.read_csv("10updated_file.csv")

# Özellik ve hedef sütunları
features = ['PTS', 'AST', 'TRB', 'FG%', 'MP']
target = 'MVP'

# Eksik değerleri doldur
imputer = SimpleImputer(strategy='mean')
scaled_features = imputer.fit_transform(df_10[features])

# StandardScaler uygula
scaler = StandardScaler()
scaled_features = scaler.fit_transform(scaled_features)

# Yeni DataFrame oluştur (ölçeklenmiş değerler + Player, Season, MVP)
scaled_df = pd.DataFrame(scaled_features, columns=features)
scaled_df['Player'] = df_10['Player']
scaled_df['Season'] = df_10['Season']
scaled_df['MVP'] = df_10['MVP']

# Yeni CSV dosyasını kaydet
scaled_df.to_csv("scaled_10updated_file.csv", index=False)

# 🔮 MODEL TAHMİNİ

# Yeni veriyi oku
df_scaled = pd.read_csv("scaled_10updated_file.csv")
years = sorted(df_scaled['Season'].unique())

X = df_scaled[features]
y = df_scaled['MVP']

# Model listesi
models = {
    "Random Forest": RandomForestClassifier(random_state=42),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss'),
    "Logistic Regression": LogisticRegression(max_iter=1000)
}

# Her model için tahmin yap
for model_name, model in models.items():
    model.fit(X, y)
    correct_predictions = 0
    print(f"\n===== {model_name} Tahminleri =====")

    y_true_all = []
    y_pred_all = []

    for year in years:
        year_data = df_scaled[df_scaled['Season'] == year].copy()
        X_year = year_data[features]

        probs = model.predict_proba(X_year)[:, 1]
        max_prob_index = probs.argmax()
        predicted_mvp = year_data.iloc[max_prob_index]['Player']
        actual_mvp = year_data[year_data['MVP'] == 1]['Player'].values[0]

        print(f"{year} - Tahmin: {predicted_mvp} | Gerçek: {actual_mvp}")

        # Doğruluk kontrolü
        if predicted_mvp == actual_mvp:
            correct_predictions += 1

        # Precision için tahminleri biriktir
        y_true = [1 if player == actual_mvp else 0 for player in year_data['Player']]
        y_pred = [1 if i == max_prob_index else 0 for i in range(len(year_data))]

        y_true_all.extend(y_true)
        y_pred_all.extend(y_pred)

    # Precision hesapla (pozitif sınıf: MVP=1)
    precision = precision_score(y_true_all, y_pred_all, pos_label=1)

    print(f"✅ Doğru tahmin sayısı: {correct_predictions} / {len(years)}")
    print(f"🎯 Precision (Pozitif sınıf - MVP=1): {precision:.4f}")
