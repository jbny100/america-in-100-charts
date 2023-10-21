"""Matplotlib chart showing total cumulative nonmilitary U.S. foreign aid from 1980-2020"""

import matplotlib.pyplot as plt 

amount = [36, 250, 411, 732, 982]
year = [1980, 1990, 2000, 2010, 2018]

plt.style.use('Solarize_Light2')

fig, ax = plt.subplots(figsize=(15, 9))

ax.plot(year, amount, linewidth=3)

ax.fill_between(year, amount, color='black')

# Place text in chart
text_x = 2010
text_y = amount[year.index(2010)] / 2

ax.text(text_x, text_y, 'U.S. Foreign Aid\nin Dollars (nonmilitary)', color='white', ha='center', va='center', fontsize=16)

# Set labels and titles

ax.set_title('Cumulative U.S. Foreign Aid\nNonmilitary Expenditure', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('', fontsize=16)

# Specify tick locations, labels and ranges

ax.set_xticks(year)
ax.set_xticklabels(year)

ax.set_xlim(left=1980, right=2018)

y_ticks = [250, 500, 750, 1000]
y_labels = ['$250B', '$500B', '$750B', '$1T']

ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)

ax.set_ylim(bottom=0, top=1000)

# Style the tick marks and set the size of the tick labels
ax.tick_params(axis='both', labelsize=14)

# Add gridlines
ax.grid(which='major', axis='y', linestyle='-', color='grey')

# ax.legend(loc='upper right')

# Hide or show the right, top or left spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)


plt.savefig('foreignaidNonMilitary.png', bbox_inches='tight')

plt.show()












