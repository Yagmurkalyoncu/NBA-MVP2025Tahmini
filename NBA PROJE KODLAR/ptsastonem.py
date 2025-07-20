import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("grafik.csv")
df['Season'] = df['Season'].astype(str)
mvp_avg = df[df['MVP'] == 1].groupby('Season')[['PTS', 'AST', 'TRB']].mean()

mvp_avg.plot(kind='line', marker='o')
plt.title("MVP'lerin Yıllara Göre Ortalama Performansı")
plt.ylabel("Değerler")
plt.xlabel("Sezon")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()