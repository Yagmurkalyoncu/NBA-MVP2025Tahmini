import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_mvp_ast_analysis_chart(csv_file_path):
    df = pd.read_csv(csv_file_path)
    
    # MVP oyuncuların sezon başı ortalama asist sayısı
    mvp_ast_by_year = df[df['MVP'] == 1].groupby('Season')['AST'].mean()
    
    # Non-MVP oyuncuların sezon başı ortalama, max ve min asist sayıları
    non_mvp = df[df['MVP'] == 0]
    non_mvp_avg_ast = non_mvp.groupby('Season')['AST'].mean()
    non_mvp_max_ast = non_mvp.groupby('Season')['AST'].max()
    non_mvp_min_ast = non_mvp.groupby('Season')['AST'].min()
    
    plt.figure(figsize=(12, 8))
    
    plt.plot(mvp_ast_by_year.index, mvp_ast_by_year.values, 
             color='blue', linewidth=2, label='Avg AST of MVP')
    
    plt.plot(non_mvp_avg_ast.index, non_mvp_avg_ast.values, 
             color='red', linewidth=2, label='Avg AST of Non-MVP')
    
    plt.plot(non_mvp_max_ast.index, non_mvp_max_ast.values, 
             color='black', linestyle='--', linewidth=1.5, label='Max AST of Non-MVP')
    
    plt.plot(non_mvp_min_ast.index, non_mvp_min_ast.values, 
             color='black', linestyle='--', linewidth=1.5, label='Min AST of Non-MVP')
    
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Assists', fontsize=12)
    plt.title('MVP vs Non-MVP Assists per Season Analysis', fontsize=14, fontweight='bold')
    
    plt.ylim(0, max(non_mvp_max_ast.max(), mvp_ast_by_year.max()) + 5)
    plt.xlim(df['Season'].min(), df['Season'].max())
    
    years = np.arange(df['Season'].min(), df['Season'].max() + 1, 2)
    plt.xticks(years)
    
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)
    plt.tight_layout()
    plt.show()

# Fonksiyon çağrısı
create_mvp_ast_analysis_chart("grafik.csv")
