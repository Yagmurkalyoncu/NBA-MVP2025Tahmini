import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Veriyi yükle
df = pd.read_csv("grafik.csv")

# Gerekli sütunlar ve sezon filtreleme
df = df[['Season', 'Age', 'MVP']]
df = df[(df['Season'] >= 2004) & (df['Season'] <= 2025)]

# MVP oyuncuların yaş ortalaması yıllara göre
mvp_age_by_year = df[df['MVP'] == 1].groupby('Season')['Age'].mean()

# Non-MVP oyuncuların yaş ortalaması yıllara göre
non_mvp_age_by_year = df[df['MVP'] == 0].groupby('Season')['Age'].mean()

# Grafik çizimi
plt.figure(figsize=(12, 6))

# MVP yaş çizgisi
plt.plot(mvp_age_by_year.index, mvp_age_by_year.values, label='Age of MVP', color='blue', linewidth=2)

# Non-MVP yaş ortalaması çizgisi
plt.plot(non_mvp_age_by_year.index, non_mvp_age_by_year.values, label='Average Age of non-MVPs', color='orange', linewidth=2)

# X ekseni 2'şer 2'şer artacak şekilde ayarla
years = np.arange(2004, 2026, 2)
plt.xticks(years)

# Grafik ayarları
plt.xlabel('Year')
plt.ylabel('Age')
plt.title('Yıllara Göre MVP ve Non-MVP Oyuncuların Ortalama Yaşları')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
