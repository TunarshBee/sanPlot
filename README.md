# **adisPlot.**
A python library that enhance the efficiency and effectiveness of data visualization. The package enables data scientists to visualize and deliver insights quickly, robustly, and in a clear and visually appealing manner.

#   Getting Started
###  With Python and Pip
Make sure you have `vscode` (or any other text editor), `python` programming language and updated `pip` package mananger installed on your local machine. With the stated conditions being met, continue down below for get started. You might want to install `pandas` to test out the package using the test files in the in the repository.

##  [Download the package](https://github.com/TunarshBee/sanPlot/dist/adisPlot-1.0.tar.gz)

After downloading the package successfully, you can either install the package globally by openning your **Download** folder and running the below command in your command prompt:
```python
pip install adisPlot-1.0.tar.gz
```

 **_OR_** 

create a virtual environment in the folder you want to use the package, copy the package into the folder and run the above command.

> **Note**: Installing the package requires you to be connected to the internet, if not you will be getting an error.

After installing the package, you can go on and create a new python file (_let say `demo.py`_) and paste any of the below type of chart to see the example usage. You can also customize the chart to your own liking.



##  Available Data Visualization and Their Usage.
The provided documentation defines several visualization for creating different types of plots using adisPlot library in Python. The visualization include:

### _**Line**:_ 
    This visualization creates a line plot with y-axis plotted against the x-axis.

#### `class Line`

**Parameters:**
- `x_values`: List of x-axis values.
- `y_values`: List of y-axis values.
- `title`: Title of the chart (optional).
- `x_ttl`: Label for the x-axis (optional).
- `y_ttl`: Label for the y-axis (optional).
- `color`: Color of the line (optional).
- `lnStyle`: Line style (optional).
- `marker`: Marker style (optional).
- `linewidth`: Width of the line (optional).
- `label`: Label for the legend (optional).
- `cmcStyle`: Boolean indicating whether to use CMC style (optional).
- `graphStyle`: Matplotlib style for the plot (optional).
- `save`: File path to save the chart image (optional).
- `grid`: Boolean indicating whether to show grid lines (optional).

**Methods:**
- `render()`: Renders the line chart with specified settings.

## Example Usage
```python
# import the package
from adisPlot.charts import Line

# creating variables for plotting y against x axis
x = [5, 2, 6, 3, 4, 6, 7, 4, 8,1, 2, 3, 4, 5, 5, 7, 4, 7,1, 2, 3, 4, 5, 5, 7, 4, 7]
y= [1, 2, 3, 4, 5, 5, 7, 4, 7,5, 2, 6, 3, 4, 6, 7, 4, 8,1, 2, 3, 4, 5, 5, 7, 4, 7]

# to use the Line chart, all you need to do is to create an object with the following properties
LineChart = Line(x, y, "Line Chart") # The third property "Line Chart" denotes the chart title

# to show the chart, you just need to call the object's render method.
LineChart.render()
```

After pasting the above example code in your `demo.py` file, all you need to do is run the python code and you should see the output as below:

![LineChart.png](/public/images/lineChart.png)


### _**Bar**:_ 
### Bar Chart
A customizable class for generating bar charts.

#### `class Bar`

**Parameters:**
- `x_values`: List of x-axis values.
- `y_values`: List of y-axis values.
- `title`: Title of the chart (optional).
- `x_ttl`: Label for the x-axis (optional).
- `y_ttl`: Label for the y-axis (optional).
- `label`: Label for the legend (optional).
- `graphStyle`: Matplotlib style for the plot (optional).
- `cmcStyle`: Boolean indicating whether to use CMC style (optional).
- `color`: Color of the bars (optional).
- `save`: File path to save the chart image (optional).
- `alpha`: Transparency of the bars (optional).
- `width`: Width of the bars (optional).
- `idxwidth`: Index width for plotting multiple bar charts (optional).

**Methods:**
- `render()`: Renders the bar chart with specified settings.
## Example Usage
```python
# Sample data
products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [1200, 1800, 900, 1500]
# Create a Bar instance and render the bar chart
from express_plotting import Bar
bar_chart = Bar(products,sales,title='Sales Performance by Product',x_ttl='Products',y_ttl='Sales',color='teal',save='barchart.png')
bar_chart.render()
```
After replacing the above example code in your `demo.py` file, you can run the code again and you should see the output as below:

![BarChart.png](/public/images/barchart.png)
### _**Scatter**:_ This visualization creates a scatter plot.

A customizable class for generating scatter plots.

#### `class Scatter`

**Parameters:**
- `x_values`: List of x-axis values.
- `y_values`: List of y-axis values.
- `title`: Title of the chart.
- `x_ttl`: Label for the x-axis (optional).
- `y_ttl`: Label for the y-axis (optional).
- `color`: Color of the markers (optional).
- `marker`: Marker style (optional).
- `label`: Label for the legend (optional).
- `cmcStyle`: Boolean indicating whether to use CMC style (optional).
- `graphStyle`: Matplotlib style for the plot (optional).
- `save`: File path to save the chart image (optional).
- `alpha`: Transparency of markers (optional).
- `linewidth`: Width of marker edge lines (optional).
- `cbar`: Color bar label (optional).
- `cmap`: Colormap for color mapping (optional).
- `size`: Marker size (optional).
- `logscalex`: Boolean indicating whether to use log scale for x-axis (optional).
- `logscaley`: Boolean indicating whether to use log scale for y-axis (optional).
- `edgcolor`: Edge color of markers (optional).

**Methods:**
- `render()`: Renders the scatter plot with specified settings.
## Example Usage
```python
# Sample data
hours_studied = [3, 2, 5, 4, 6, 5, 7, 6, 8, 7]exam_scores = [70, 65, 80, 75, 85, 78, 90, 82, 92, 88]
# Create a Scatter instance and render the scatter plot
from express_plotting import Scatter

scatter_plot = Scatter(
x_values=hours_studied,
y_values=exam_scores,
title='Exam Scores vs. Hours Studied',
x_ttl='Hours Studied',
y_ttl='Exam Scores',
color='red',
marker='x',
alpha=0.8,
save='/public/images/scatter_plot.png'
)
scatter_plot.render()
```
After replacing the above example code in your `demo.py` file, you can run the code again and you should see the output as below:

![ScatterPlot.png](/public/images/scatter_plot.png)


### Pie Chart
A customizable class for generating pie charts.

#### `class Pie`

**Parameters:**
- `values`: List of values for each slice.
- `labels`: Labels for each slice (optional).
- `title`: Title of the chart (optional).
- `colors`: Colors for each slice (optional).
- `explode`: Explode values for slices (optional).
- `save_path`: File path to save the chart image (optional).

**Methods:**
- `render()`: Renders the pie chart with specified settings.
## Example Usage
```python
values = [30, 20, 25, 15, 10]
labels = ["Label 1", "Label 2", "Label 3", "Label 4", "Label 5"]
colors = ["#FF9999", "#66B2FF", "#99FF99", "#FFCC99", "#C2C2f2"]
explode = (0.1, 0, 0, 0, 0)  # Explode the first slice


# Example usage for PieChart (inherits from DoughnutChart)
pie_chart = Pie(values, labels=labels, title="Pie Chart Example", colors=colors, explode=explode, save_path="pie_chart.png")
pie_chart.render()
```

After replacing the above example code in your `demo.py` file, you can run the code again and you should see the output as below:

![Pie Chart.png](/public/images/pie_chart.png)

## _**Circle_paking_chart**:_ 
#### This visualization creates a circular packing visualization.
## Example Usage
```python
# Sample data
data = [
{
"id": "World",
"datum": 6964195249,
"children": [
{
"id": "North America",
"datum": 450448697,
"children": [
{"id": "United States", "datum": 308865000},
{"id": "Mexico", "datum": 107550697},
{"id": "Canada", "datum": 34033000},
],
},
{
"id": "South America",
"datum": 278095425,
"children": [
{"id": "Brazil", "datum": 192612000},
{"id": "Colombia", "datum": 45349000},
{"id": "Argentina", "datum": 40134425},
],
},# ... Other continents and countries data ...
],
}
]
# Create a CirclePacking instance and render the circle packing chart
from express_plotting import CirclePacking
circle_packing_chart = CirclePacking(data)
circle_packing_chart.compute_circle_positions()
circle_packing_chart.render()
```

After replacing the above example code in your `demo.py` file, you can run the code again and you should see the output as below:

![Circle Packing Chart.png](/public/images/circle_packing.png)
### _**NetworkViz**:_ This visualization creates a hierarchical network visualization.


# Heatmap 

The `Heatmap` class provides a simple way to create customizable heatmaps using the Matplotlib library in Python. With this class, you can visualize two-dimensional data matrices as colored grids. The class allows you to customize various aspects of the heatmap, such as data, labels, color map, title, and more.


### `Heatmap`

The `Heatmap` class is designed to facilitate the creation of customizable heatmaps. It provides the following parameters for customization:

- `data`: A 2D NumPy array representing the data to be visualized as a heatmap.
- `x_labels`: A list of labels for the x-axis ticks (optional).
- `y_labels`: A list of labels for the y-axis ticks (optional).
- `title`: The title of the heatmap (optional).
- `cmap`: The colormap to be used for coloring the heatmap (default: "viridis").
- `colorbar`: A boolean indicating whether to display a colorbar (default: False).
- `save_path`: The file path for saving the heatmap as an image (optional).

### `render()`

The `render()` method generates and displays the heatmap based on the provided parameters. It performs the following actions:

1. Uses Matplotlib to visualize the data as a colored grid.
2. Optionally adds x-axis and y-axis labels.
3. Sets the title of the heatmap.
4. Optionally adds a colorbar for interpreting the colormap.
5. Optionally saves the heatmap as an image file.

## Example Usage

```python
from adisPlot.charts import Heatmap


# Create example data and labels
data = np.random.rand(5, 7)
x_labels = ["Label 1", "Label 2", "Label 3", "Label 4", "Label 5"]
y_labels = ["Category A", "Category B", "Category C", "Category D", "Category E", "Category F", "Category G"]

# Initialize a Heatmap instance

heatmap = Heatmap(data, x_labels=x_labels, y_labels=y_labels, title="Custom Heatmap Example", cmap="YlOrRd", colorbar=True, save_path="heatmap.png")

# Generate and display the heatmap
heatmap.render()
```
After replacing the above example code in your `demo.py` file, you can run the code again and you should see the output as below:

![Heat Map.png](/public/images/heatmap.png)

## Customization

1. Replace `data` with your own 2D data array.
2. Customize `x_labels` and `y_labels` lists to match your data dimensions.
3. Modify `title` to set the heatmap title.
4. Adjust the `cmap` parameter to choose a different colormap from Matplotlib's colormap options.
5. Set `colorbar` to `True` if you want to display a colorbar.
6. Provide a `save_path` to save the heatmap as an image.
