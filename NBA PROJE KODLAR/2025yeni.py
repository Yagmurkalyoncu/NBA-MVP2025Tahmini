import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import warnings

# Uyarıları bastır
warnings.filterwarnings("ignore")

# 🔹 Veriyi yükle
df_20 = pd.read_csv("2025tahmini.csv")

# 🔹 Kullanılacak özellikler ve etiket
features = ['PTS', 'AST', 'TRB', 'FG%', 'MP']
X = df_20[df_20['Season'] < 2025][features]  # Eğitim verisi (2005–2025)
y = df_20[df_20['Season'] < 2025]['MVP']

# 🔹 Eksik verileri ortalama ile doldur
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# 🔹 Veriyi standardize et
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

# 🔹 Modeli eğit
model = RandomForestClassifier(random_state=42)
model.fit(X_scaled, y)

# 🔹 2025 sezon verisini hazırla
df_2025 = df_20[df_20['Season'] == 2025].copy()
X_2025_imputed = imputer.transform(df_2025[features])
X_2025_scaled = scaler.transform(X_2025_imputed)

# 🔹 Olasılık tahmini yap
probs = model.predict_proba(X_2025_scaled)[:, 1]
top5_indices = probs.argsort()[-5:][::-1]

# 🔹 Sonuçları yazdır
print("🎯 2025 Yılı Most Valuable Player (MVP) Tahmin Listesi – Random Forest")
for rank, idx in enumerate(top5_indices, start=1):
    player_name = df_2025.iloc[idx]['Player']
    player_prob = probs[idx]
    print(f"{rank}. {player_name} (Olasılık: {player_prob:.4f})")
