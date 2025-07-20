import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_mvp_analysis_chart(csv_file_path):
    df = pd.read_csv(csv_file_path)
    
    # Yıllara göre MVP oyuncuların ortalama puanı (PTS) - Burada oyuncu başına maç sayısı yoksa toplam puan ortalaması
    mvp_pts_by_year = df[df['MVP'] == 1].groupby('Season')['PTS'].mean()
    
    # Non-MVP oyuncular için yıllık ortalama, max ve min puanlar
    non_mvp = df[df['MVP'] == 0]
    non_mvp_avg_pts = non_mvp.groupby('Season')['PTS'].mean()
    non_mvp_max_pts = non_mvp.groupby('Season')['PTS'].max()
    non_mvp_min_pts = non_mvp.groupby('Season')['PTS'].min()
    
    plt.figure(figsize=(12, 8))
    
    plt.plot(mvp_pts_by_year.index, mvp_pts_by_year.values, 
             color='blue', linewidth=2, label='Avg PTS of MVP')
    
    plt.plot(non_mvp_avg_pts.index, non_mvp_avg_pts.values, 
             color='red', linewidth=2, label='Avg PTS of Non-MVP')
    
    plt.plot(non_mvp_max_pts.index, non_mvp_max_pts.values, 
             color='black', linestyle='--', linewidth=1.5, label='Max PTS of Non-MVP')
    
    plt.plot(non_mvp_min_pts.index, non_mvp_min_pts.values, 
             color='black', linestyle='--', linewidth=1.5, label='Min PTS of Non-MVP')
    
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Points', fontsize=12)
    plt.title('MVP vs Non-MVP Points per Season Analysis', fontsize=14, fontweight='bold')
    
    plt.ylim(0, max(non_mvp_max_pts.max(), mvp_pts_by_year.max()) + 10)
    plt.xlim(df['Season'].min(), df['Season'].max())
    
    # X ekseninde 2 yıl aralıkla gösterim için:
    years = np.arange(df['Season'].min(), df['Season'].max() + 1, 2)
    plt.xticks(years)
    
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)
    plt.tight_layout()
    plt.show()

# Fonksiyonu çağırırken csv dosyasını ver
create_mvp_analysis_chart("grafik.csv")
