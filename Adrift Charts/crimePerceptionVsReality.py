"""Side-by-side line graphs showing the different between perception vs. reality of U.S.
crime rate from 1993 to 2015.
"""

import matplotlib.pyplot as plt 

years = [1993, 1998, 2003, 2009, 2015]
perception = [85.7, 41, 53.6, 74.2, 69.6]
reality =[80.3, 50, 28.6, 17.6, 17.7]
y_ticks = [25, 50, 75, 100]

# Years to be displayed on the x-axis
x_ticks = [1993, 2003, 2015]

# In terminal type import matplotlib.pyplot as plt, 
# plt.style.available to see available chart styles.
plt.style.use('seaborn-v0_8-dark-palette')

# Sets two side-by-side charts
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot perception on the left subplot
axs[0].plot(years, perception, color='darkgreen', linewidth=3)
#axs[0].set_title('% saying there is more\n crime than a years ago')

# Plot reality on the right subplot
axs[1].plot(years, reality, color='blue', linewidth=3)
#axs[1].set_title('Violent crimes per 1,000\n people ages 12 and older')

# For each axis, set x and y ticks and labels, grid and title
for ax in axs:
	ax.set_xticks(x_ticks)
	ax.set_xlabel('')
	y_ticks = [25, 50, 75, 100]
	y_labels = [f"{y}%" for y in y_ticks]
	ax.set_yticks(y_ticks)
	ax.set_yticklabels(y_labels)
	ax.set_ylim(0, 100)
	ax.grid(which='both', axis='y', linestyle='-', color='grey', linewidth=0.5)
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.spines['left'].set_visible(False)

# Add custom legend using text
axs[0].text(1992, 105, "% saying there is more\n crime than a year ago", 
	color='darkgreen', fontsize=10)
axs[1].text(1992, 105, "Violents crimes per 1,000\n people ages 12 and older", 
	color='blue', fontsize=10)

# Overall title for the figure
fig.suptitle('Perception vs. Reality of U.S. Crime Rate', fontsize=16)

# Adjust the space between subplots
plt.tight_layout(pad=4)

# Legend shows what each line is.
# ax.legend(loc='upper right')

fig.savefig('crimePerceptionVsReality.png', bbox_inches='tight', dpi=300)

plt.show()

