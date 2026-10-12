import matplotlib.pyplot as plt
import numpy as np

# Set math text font to Computer Modern (LaTeX standard)
plt.rcParams['mathtext.fontset'] = 'cm'

# Data
categories = ['Jan15', 'Feb15', 'Mar15', 'Apr15']
series1 = np.array([3, 4, 5, 3])
series2 = np.array([1, 2, 2, 5])
series3 = np.array([2, 3, 3, 4])

fig, ax = plt.subplots(figsize=(8, 5))

# Plotting stacked bars
ax.bar(categories, series1, label='Series 1', color='crimson')
ax.bar(categories, series2, bottom=series1, label='Series 2', color='steelblue')
ax.bar(categories, series3, bottom=series1 + series2, label='Series 3', color='forestgreen')

# Formatting
ax.set_title("Multiseries Stacked Bar Chart", fontsize=13, weight='bold')
ax.set_ylabel("Values")
ax.legend()

plt.tight_layout()
plt.show()
