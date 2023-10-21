
# Chart showing the numbers and percentage increase of migrants every 5 years.

from plotly.graph_objs import Bar, Scatter, Layout
from plotly import offline

x_values = [1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 
	2010,2015, 2019]

y_values_bar = [85, 90, 102, 113, 153, 161, 174, 192, 221, 249, 272]
y_values_line = [2.1, 2.15, 2.15, 2.57, 2.78, 2.71, 2.72, 2.85, 3.31, 3.42, 3.57] 

# Convert y_values for the bars to string and append 'M'
text_values = [str(value) + 'M' for value in y_values_bar]

# Bar data

bar = Bar(
	x=x_values, 
	y=y_values_bar, 
	text=text_values, # Display these values as text
	textposition='outside',  #place text above the bars
	yaxis ='y2',   # Assign to a secondary y-axis
	name="international Migrants")  # Sets the legend label

# Line data
line = Scatter(
	x=x_values, 
	y=y_values_line, 
	mode='lines',
	name="As a percentage of the world's population", 
	line=dict(color='black', width=3))

data = [bar, line]


x_axis_config = {'title': '', 'dtick': 5}
y_axis_config = {
	'title': '', 
	'tickvals': [1, 2, 3, 4],
	'ticktext': ['1%', '2%', '3%', '4%'],  # What text to show for the tickvals
	'range': [0, 4], 
	'side': 'right',
	'gridcolor': 'gray',
	'zeroline': False
	}

y_axis_config_2 = {
	'title': '',
	'side': 'left',
	'overlaying': 'y',
	'range': [0, 300],
	'showticklabels': False,  # Hide tick labels for yaxis2
	'showgrid': False  # Hide gridlines for yaxis2 
}

my_layout = Layout(title='Percent Increase of Migrants Every Five Years',
	xaxis=x_axis_config, yaxis=y_axis_config, yaxis2=y_axis_config_2)

offline.plot({'data': data, 'layout': my_layout}, filename='freedomOfMovement.html')
