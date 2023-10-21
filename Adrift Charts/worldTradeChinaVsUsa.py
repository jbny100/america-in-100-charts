
"""Chart showing the growing market share of China over the US 
as the world's most popular trading partner.
"""

import matplotlib.pyplot as plt 

percentage = [81.3, 68.8, 41.7, 33.3, 29.2]
year = [2000, 2005, 2010, 2015, 2020]

# In terminal type import matplotlib.pyplot as plt, 
# plt.style.available to see available chart styles.
plt.style.use('Solarize_Light2')

# subplots() function generates one or more plots in the same figure.
# 'fig' represents the entire figure or collection of plots 
# 'ax' represents a single plot in the figure.

# fig, ax = subplots()
fig, ax = plt.subplots(figsize=(15, 9))

# Plotting a line graph showing the US percentage of market share 
# from 2000 to 2020.

ax.plot(year, percentage, linewidth=3)

# Fill the area beneath the line with black fill.
ax.fill_between(year, percentage, color='black')

# Place the 'U.S.' text.
text_x = 2010
text_y = percentage[year.index(2010)] / 2

ax.text(text_x, text_y, 'U.S.', color='white', ha='center', va='center', fontsize=16)

# Place the 'China' text
china_text_x = 2010
china_text_y = (percentage[year.index(2010)] + 100) / 2

ax.text(china_text_x, china_text_y, 'China', color='black', ha='center', va='center', fontsize=16)

# Set labels and titles.

ax.set_title("Share of Countries with Largest Trade \nPartner: China vs. U.S.", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('', fontsize=16)


# Specify 'year' as tick locations and labels.

ax.set_xticks(year)
ax.set_xticklabels(year) 

# Set x-axis range
ax.set_xlim(left=2000, right=2020)

# Set y-axis ticks, labels and limits

y_ticks = [25, 50, 75, 100]
y_labels = [f"{y}%" for y in y_ticks]

ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)

# Set y-axis range
ax.set_ylim(bottom=0, top=100)

# The tick_params() method styles the tick marks and sets the size of the tick labels.
ax.tick_params(axis='both', labelsize=14)

# Add gridlines
ax.grid(which='major', axis='y', linestyle='-', color='grey')

# Legend shows what each line is.
# ax.legend(loc='upper right')

# Hide or show the right, top or left spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)

# Only show ticks on the left and bottom spines. 
#ax.yaxis.set_ticks_position('left')
#ax.xaxis.set_ticks_position('bottom')

#plt.show()
plt.savefig('worldTradeChinaUs.png', bbox_inches='tight')























