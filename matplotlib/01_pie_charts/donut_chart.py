import matplotlib.pyplot as plt

# Set math text font to Computer Modern (LaTeX standard)
plt.rcParams['mathtext.fontset'] = 'cm'

labels = ['Nokia', 'Samsung', 'Apple', 'Lumia']
values = [10, 30, 45, 15]
colors = ['gold', 'forestgreen', 'crimson', 'steelblue']

fig, ax = plt.subplots(figsize=(6, 6))

wedges, texts, autotexts = ax.pie(
    values,
    labels=labels,
    colors=colors,
    autopct=lambda pct: f"{pct:.1f}%",
    startangle=90,
    wedgeprops={'width': 0.4, 'edgecolor': 'white'}
)

for t in texts:
    t.set_fontsize(11)
for at in autotexts:
    at.set_fontsize(10)
    at.set_weight('bold')

ax.set_title("Market Share (Donut Chart)", fontsize=13, weight='bold')

plt.tight_layout()
plt.show()
