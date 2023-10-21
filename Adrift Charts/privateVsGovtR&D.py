# Chart showing the disparity between employee productivity 
# and hourly compensation over time.

import matplotlib.pyplot as plt

private = [0.59, 1.0, 1.0, 1.37, 1.81, 1.68, 2.12]
govt = [0.68, 1.5, 1.12, 1.12, 0.62, 0.87, 0.62]
year = [1953, 1970, 1980, 1990, 2000, 2010, 2019]

plt.style.use('tableau-colorblind10')

fig, ax = plt.subplots(figsize=(15, 9))

# Plotting the 'private' spending data with blue color (default).
ax.plot(year, private, label='Private', linewidth=3, marker='o')

# Plotting the 'govt' spending data with red color.
ax.plot(year, govt, c='red', label='Government', linewidth=3, marker='o')

# Setting labels and titles

ax.set_title("U.S. R&D as Percentage of GDP, \nby Source of Funding", fontsize=24)

ax.set_xlabel('', fontsize=16)
ax.set_ylabel('', fontsize=16)


# Specify the years as tick locations and labels.
ax.set_xticks(year)
ax.set_xticklabels(year)

# Set x-axis range.
ax.set_xlim(left=1952, right=2020)

# Set y-axis ticks, labels and limits.
y_ticks = [0.5, 1.0, 1.5, 2.0, 2.5]
y_labels = ["{}%".format(y) for y in y_ticks] # List comp adds % symbol to y-axis label.

ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)

ax.set_ylim(bottom=0, top=2.5)

ax.tick_params(axis='both', labelsize=14)

# Add gridlines.
ax.grid(which='major', axis='y', linestyle='-', color='grey')

# Legend shows what each line is.
ax.legend(loc='upper right')

# Hide the right, top and left spines.
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)

# Only show ticks on the left and bottom spines. 
#ax.yaxis.set_ticks_position('left')
#ax.xaxis.set_ticks_position('bottom')

plt.savefig('privateVsGovtR&D.png', bbox_inches='tight')

plt.show()






