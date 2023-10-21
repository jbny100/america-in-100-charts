# Pie chart comparison showing U.S. share of global R&D spending in 1960 vs. 2019.

import matplotlib.pyplot as plt 

# Data
years = ["1960", "2019"]
us_share = [69, 30]
world_share = [31, 70]

# Labels for the legend
labels = ["U.S.", "Rest of World"]

# Colors for the pie slices
colors = ["lightblue", "gray"]

plt.style.use('tableau-colorblind10')

# 1 row, 2 columns of subplots.
# This sets up two side-by-side pie charts 
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plotting 1960 pie chart
ax[0].pie([us_share[0], world_share[0]], colors=colors, startangle=90, autopct='%d%%', 
	textprops={'fontsize': 20})
ax[0].set_xlabel("1960", fontsize=20)

# Plotting the 2019 pie chart
ax[1].pie([us_share[1], world_share[1]], colors=colors, startangle=90, autopct='%d%%', 
	textprops={'fontsize': 20})
ax[1].set_xlabel("2019", fontsize=20)

fig.legend(labels, loc="upper left", bbox_to_anchor=(0.1, 0.95))

# Set the main title for the entire figure
fig.suptitle("U.S. Share of Global R&D Spending", fontsize=24)

# Adjust the layout
plt.tight_layout()

# Ensure the title doesn't overlap with the pie charts
plt.subplots_adjust(top=0.85)

fig.savefig('globalR&dSpending.png', bbox_inches='tight')
plt.show()


