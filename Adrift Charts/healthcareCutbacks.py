# Line graph showing the decline in psychiatric inpatient beds from 1970 to 2014.

import matplotlib.pyplot as plt 

years = [1970, 1980, 1990, 2000, 2010, 2014]
beds = [475, 225, 225, 180, 165, 165]

plt.style.use('tableau-colorblind10')

fig, ax = plt.subplots(figsize=(15, 9))

ax.plot(years, beds, linewidth=3, marker='o', markersize=8, markeredgecolor='blue',
	markerfacecolor='yellow', label='Data Points')

ax.set_title("Number of Psychiatric Inpatient Beds", fontsize=24)

ax.set_xlabel("", fontsize=16)
ax.set_ylabel("", fontsize=16)

# Specify the years as tick locations and labels
ax.set_xticks(years)
ax.set_xticklabels(years)

ax.set_xlim(left=1970, right=2014)

# Set y-axis ticks and limits
y_ticks = [100, 200, 300, 400, 500]
y_labels = ["{}K".format(y) for y in y_ticks] # List comp adds % symbol to y-axis label.

ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)

ax.set_ylim(bottom=0, top=500)

ax.tick_params(axis='both', labelsize=14)

# Add gridlines
ax.grid(which='major', axis='y', linestyle='-', color='grey')

# Legend
ax.legend(loc='upper right')


# plt.show()

plt.savefig('healthcareCutbacks.png', bbox_inches='tight')








