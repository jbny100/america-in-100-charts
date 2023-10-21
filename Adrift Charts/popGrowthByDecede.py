
"""
Histogram showing the U.S. population growth by decade since 1800
"""

import matplotlib.pyplot as plt 

decades = ["1800-1810", "1810-1820", "1820-1830", "1830-1840", "1840-1850", 
           "1850-1860", "1860-1870", "1870-1880", "1880-1890", "1890-1900",
           "1900-1910", "1910-1920", "1920-1930", "1930-1940", "1940-1950", 
           "1950-1960", "1960-1970", "1970-1980", "1980-1990", "1990-2000",
           "2000-2010", "2010-2020"]


growth = [36.5, 33, 33.5, 32.5, 36, 35.5, 23, 30.6, 25.4, 
		22.5, 22.5, 15, 16.5, 6, 14.6, 18.8, 10, 14,
		10, 14, 10, 6.7]

# Get both a figure and ax object
fig, ax = plt.subplots(figsize=(15, 9))


# Create a horizontal bar chart
# Reverse the lists to have the earliest decade at the top
ax.barh(decades[::-1], growth[::-1], color='blue')


# Arrow Annotation

# The position of the arrow on the graph.

# adjusted to account for reversed bars
start_decade_index = len(decades) - 1 - decades.index("1900-1910")
end_decade_index = len(decades) - 1 - decades.index("2010-2020")

start_point = 29.5 
end_point = 15

# Annotate with an arrow
ax.annotate('', 
            xy=(end_point, end_decade_index), 
           	xytext=(start_point, start_decade_index), 
            arrowprops=dict(facecolor='red', arrowstyle='->', lw=1.5), 
            )


# Set the labels and title
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_title('U.S. Population Growth by Decade', fontsize=22)



# Set growth ticks, labels, and limits

g_ticks = [10, 20, 30, 40]
g_labels = [f"{g}%" for g in g_ticks]


ax.set_xticks(g_ticks)
ax.set_xticklabels(g_labels) 

# The tick_params() method styles the tick marks and sets the size of the tick labels.
ax.tick_params(axis='both', labelsize=14)

# Add gridlines
plt.grid(which='major', axis='x', linestyle='-', color='grey')

# Hide or show the right, top or left spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(True)


# Only show ticks on the left and bottom spines. 
#ax.yaxis.set_ticks_position('left')
#ax.xaxis.set_ticks_position('bottom')


# Legend shows what each line is.
# ax.legend(loc='upper right')


# Display and save the chart to a png file.
plt.tight_layout()
plt.savefig('popGrowthByDecade.png', bbox_inches='tight')
plt.show()

