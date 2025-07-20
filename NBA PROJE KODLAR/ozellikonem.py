import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

# Varsayalım df hazır ve içinde aşağıdaki sütunlar var:
# ['MP', 'PTS', 'AST', 'TRB', 'FG%', 'MVP']
df = pd.read_csv("grafik.csv")
# Özellikler ve hedef
features = ['MP', 'PTS', 'AST', 'TRB', 'FG%']
X = df[features]
y = df['MVP']

# Modeli oluşturduk ve eğittik
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Özellik önemlerini aldık
importances = model.feature_importances_

# DataFrame'e çevir
feat_imp = pd.DataFrame({'Feature': features, 'Importance': importances})

# Önem değerlerine göre sırala
feat_imp = feat_imp.sort_values(by='Importance')

# Yatay bar grafiği çiz
plt.figure(figsize=(8,5))
sns.barplot(x='Importance', y='Feature', data=feat_imp, palette='viridis')
plt.title('MVP Tahmininde Özelliklerin Önem Düzeyi')
plt.xlabel('Özellik Önemi')
plt.ylabel('Özellik')
plt.tight_layout()
plt.show()