import matplotlib.pyplot as plt

# Yıllar
years = list(range(2004, 2025))

# Gerçek MVP'ler
true_mvp = [
    "Kevin Garnett", "Steve Nash", "Steve Nash", "Dirk Nowitzki", "Kobe Bryant",
    "LeBron James", "LeBron James", "Derrick Rose", "LeBron James", "LeBron James",
    "Kevin Durant", "Stephen Curry", "Stephen Curry", "Russell Westbrook", "James Harden",
    "Giannis Antetokounmpo", "Giannis Antetokounmpo", "Nikola Jokic", "Nikola Jokic",
    "Joel Embiid", "Nikola Jokic"
]

# XGBoost Tahminleri
predicted_mvp_xgb = [
    "Kevin Garnett", "Steve Nash", "Steve Nash", "Dirk Nowitzki", "Kobe Bryant",
    "LeBron James", "LeBron James", "Derrick Rose", "LeBron James", "Kevin Durant",
    "Kevin Durant", "Stephen Curry", "Stephen Curry", "Russell Westbrook", "James Harden",
    "Giannis Antetokounmpo", "Giannis Antetokounmpo", "Nikola Jokic", "Nikola Jokic",
    "Luka Doncic", "Nikola Jokic"
]

# Benzersiz oyuncuları sayısal eksene eşle
unique_players = list(set(true_mvp + predicted_mvp_xgb))
player_to_y = {player: i for i, player in enumerate(sorted(unique_players))}

# Y ekseni konumları
true_y = [player_to_y[player] for player in true_mvp]
pred_y = [player_to_y[player] for player in predicted_mvp_xgb]

# Grafik oluştur
plt.figure(figsize=(16, 10))

# Gerçek MVP noktaları
plt.scatter(years, true_y, color='green', marker='o', s=100, label='Gerçek MVP', zorder=3)

# Tahmin noktaları
for i in range(len(years)):
    if true_mvp[i] == predicted_mvp_xgb[i]:
        plt.scatter(years[i], pred_y[i], marker='x', color='blue', s=150,
                    linewidth=3, label='Doğru Tahmin' if i == 0 or 'Doğru Tahmin' not in plt.gca().get_legend_handles_labels()[1] else "")
    else:
        plt.scatter(years[i], pred_y[i], marker='x', color='red', s=150,
                    linewidth=3, label='Yanlış Tahmin' if 'Yanlış Tahmin' not in plt.gca().get_legend_handles_labels()[1] else "")

# Eksen ayarları
sorted_players = [player for player, _ in sorted(player_to_y.items(), key=lambda x: x[1])]
plt.yticks(ticks=range(len(unique_players)), labels=sorted_players)
plt.xticks(years, rotation=45)
plt.xlabel("Yıl", fontsize=12)
plt.ylabel("Oyuncular", fontsize=12)
plt.title("XGBoost MVP Tahminleri vs Gerçek MVP'ler (2004–2024)", fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)
plt.tight_layout()

plt.show()
