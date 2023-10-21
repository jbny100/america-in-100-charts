# Bar chart illustrating the surge in new business applications since Covid.

from plotly.graph_objs import Bar, Scatter, Layout
from plotly import offline

y_values = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 
	2018, 2019, 2020, 2021]

x_values = [2.5, 2.6, 2.6, 2.6, 2.7, 2.8, 2.9, 3.2, 3.5, 
	3.5, 4.4, 5.4]

# Bar data
bar = Bar(
	y=y_values, 
	x=x_values, 
	name="Number of Business Applications", # Sets the legend label
	orientation='h' # Horizontal bars
	)

# Add vertical line
line = Scatter(
	x=[5.4, 5.4], # x-coordinates of the line's start and end points
	y=[2010, 2021 + 0.4], # y-coordinates of the line's start and end points
	mode='lines', 
	line=dict(color='blue'), 
	showlegend=False, 
	)

data = [bar, line]

x_axis_config = {
'title': '', 
'tickvals': [1, 2, 3, 4, 5], 
'ticktext': ['1M', '2M', '3M', '4M', '5M'], 
'range': [0, 6],
'gridcolor': 'gray',
'zeroline': False
}

y_axis_config = {
	'title': '', 
	'tickvals': y_values,
	'range': [2022, 2009], # Set in decending order 
	'side': 'left',
	}


annotations = [{
'x': 5.55,  # text slightly to the right of the line
'y': (2021 + 2010) / 2,  # midpoint  
'xref': 'x',
'yref': 'y',
'text': '5.4M',
'showarrow': False, 
'font': {'size': 16, 'color': 'blue'}

}]


my_layout = Layout(
	title={
	'text': 'Number of Business Applications', 
	'font': {'size': 24}
	},
	xaxis=x_axis_config, 
	yaxis=y_axis_config, 
	annotations=annotations)


offline.plot({'data': data, 'layout': my_layout}, filename='surgingStartups.html')



