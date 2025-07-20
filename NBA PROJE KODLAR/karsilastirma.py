import matplotlib.pyplot as plt
import numpy as np

# Veri
models = ['Random Forest', 'XGBoost', 'Logistic Regression']
precision_10_years = [1.0000, 1.0000, 0.5000]
precision_20_years = [0.9524, 0.9048, 0.3810]

# Bar pozisyonları
x = np.arange(len(models))
width = 0.35

# Grafik oluştur
fig, ax = plt.subplots(figsize=(12, 8))

# Barları çiz
bars1 = ax.bar(x - width/2, precision_10_years, width, label='10 Yıllık Veri', 
               color='#2E86AB', alpha=0.8, edgecolor='black', linewidth=1)
bars2 = ax.bar(x + width/2, precision_20_years, width, label='20 Yıllık Veri', 
               color='#F24236', alpha=0.8, edgecolor='black', linewidth=1)

# Değerleri barların üzerinde göster
def add_value_labels(bars, values):
    for i, (bar, value) in enumerate(zip(bars, values)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                f'{value:.4f}', ha='center', va='bottom', 
                fontweight='bold', fontsize=11)

add_value_labels(bars1, precision_10_years)
add_value_labels(bars2, precision_20_years)

# Grafik ayarları
ax.set_xlabel('Modeller', fontsize=14, fontweight='bold')
ax.set_ylabel('Precision', fontsize=14, fontweight='bold')
ax.set_title('Model Precision Karşılaştırması: 10 Yıllık vs 20 Yıllık Veri', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=12)
ax.legend(fontsize=12, loc='upper right')

# Y ekseni ayarları
ax.set_ylim(0, 1.1)
ax.set_yticks(np.arange(0, 1.1, 0.1))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.1f}'.format(y)))

# Grid ekle
ax.grid(True, alpha=0.3, axis='y')
ax.set_axisbelow(True)

# Performans değişikliklerini vurgula
for i in range(len(models)):
    change = precision_20_years[i] - precision_10_years[i]
    if change < 0:
        # Düşüş için kırmızı metin
        ax.text(i, max(precision_10_years[i], precision_20_years[i]) + 0.08,
                f'↓ {change:.4f}', 
                ha='center', va='bottom',
                color='red', fontweight='bold', fontsize=11)
    elif change > 0:
        # Artış için yeşil metin
        ax.text(i, max(precision_10_years[i], precision_20_years[i]) + 0.08,
                f'↑ +{change:.4f}', 
                ha='center', va='bottom',
                color='green', fontweight='bold', fontsize=11)
    else:
        # Değişim yok - eşit işareti
        ax.text(i, max(precision_10_years[i], precision_20_years[i]) + 0.08,
                'Sabit', 
                ha='center', va='bottom',
                color='blue', fontweight='bold', fontsize=11)

# Layout'u optimize et
plt.tight_layout()

# Grafik istatistikleri yazdır
print("Model Performans Analizi:")
print("=" * 50)
for i, model in enumerate(models):
    change = precision_20_years[i] - precision_10_years[i]
    change_percent = (change / precision_10_years[i]) * 100 if precision_10_years[i] != 0 else 0
    print(f"{model}:")
    print(f"  10 Yıl: {precision_10_years[i]:.4f}")
    print(f"  20 Yıl: {precision_20_years[i]:.4f}")
    print(f"  Değişim: {change:+.4f} ({change_percent:+.1f}%)")
    print()

plt.show()