import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("grafik.csv")
sns.scatterplot(data=df, x='MP', y='PTS', hue='MVP', palette='Set1')
plt.title('MP vs PTS - MVP ve Non-MVP Dağılımı')
plt.xlabel('MP (Oynanan Dakika)')
plt.ylabel('PTS (Maç Başına Sayı)')
plt.legend(title='MVP')
plt.show()