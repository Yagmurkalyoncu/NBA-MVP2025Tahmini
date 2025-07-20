import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("grafik.csv")
sns.violinplot(x='MVP', y='PTS', data=df)
plt.title("MVP Olup Olmama Durumuna Göre Puan Dağılımı")
plt.show()