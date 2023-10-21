# A scatter chart showing the decline in men's share of college enrollment 
# in the U.S. since 1970.

import matplotlib.pyplot as plt 

year = [1970, 1980, 1990, 2000, 2010, 2021]
y_values = [58.3, 49.2, 45.8, 44.2, 43.3, 40.4]

# In terminal type import matplotlib.pyplot as plt, 
# plt.style.available to see available chart styles.
plt.style.use('tableau-colorblind10')

# subplots() function generates one or more plots in the same figure.
# 'fig' represents the entire figure or collection of plots 
# 'ax' represents a single plot in the figure.
fig, ax = plt.subplots(figsize=(15,9))


# Determine the color for the first point using the colormap
color_map = plt.cm.Blues
color_for_all_points = color_map(y_values[0]/60) # Normalize the value to [0, 1]

# Plot the scatter points 
ax.scatter(year, y_values, color=color_for_all_points, s=10)


# Add annotation for the last scatter point (Optional)
last_point_annotation = "{}%".format(y_values[-1])
ax.text(year[-1], y_values[-1] - 2.5, last_point_annotation, fontsize=12,
	horizontalalignment='center', verticalalignment='top', color='blue',
	bbox=dict(boxstyle="circle", fc="white", ec="blue"))


# Set chart title and label axes.
ax.set_title("Men's Share of College Enrollment in the U.S.", fontsize=20)
ax.set_xlabel(" ", fontsize=16)
ax.set_ylabel(" ", fontsize=16)

# Specify the years as tick locations and labels.
ax.set_xticks(year)
ax.set_xticklabels(year)

# Set the x_axis range
ax.set_xlim(left=1969, right=2022)

# Set y_axis ticks, labels and limits.
y_ticks = [10, 20, 30, 40, 50, 60]
y_labels = [f"{y}%" for y in y_ticks] # add a '%' sign to y+axis labels
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)

# Set the y_axis range
ax.set_ylim(bottom=0, top=60)

# The tick_params() method styles the tick marks and sets the size of the tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Add gridlines
ax.grid(which='major', axis='y', linestyle='-', color='grey')

# Hide the right, left and top spines
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)


# The first argument of savefig() is a filename for the plot image 
# The second arguemnt trims the extra whitespace from the plot.
plt.savefig('mensCollegeEnrollment.png', bbox_inches='tight')

# Show chart
plt.show()