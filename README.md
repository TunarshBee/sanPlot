# **SanPlot.**
A python library that enhance the efficiency and effectiveness of data visualization. The package enables data scientists to visualize and deliver insights quickly, robustly, and in a clear and visually appealing manner.

#   Getting Started
###  With Python and Pip
Make sure you have `python` programming language and updated `pip` package mananger. With the stated conditions being met, continue down below for get started.

##  [Download the package](https://github.com/)

After downloading the package successfully, you can either install the package globally by openning your **Download** folder and running the below command in your command prompt:
```python
pip install sanPlot-1.0.tar.gz
```

 **_OR_** 

create a virtual environment in the folder you want to use the package, copy the package into the folder and run the above command.

> **Note**: Installing the package requires you to be connected to the internet, if not you will be getting an error.

After installing the package, you can go on and create a new python file (_let say `demo.py`_) and paste the below code snippet into the file:

```python
# import the package
from sanPlot.charts import Line

# creating variables for plotting y against x axis
x = [5, 2, 6, 3, 4, 6, 7, 4, 8,1, 2, 3, 4, 5, 5, 7, 4, 7,1, 2, 3, 4, 5, 5, 7, 4, 7]
y= [1, 2, 3, 4, 5, 5, 7, 4, 7,5, 2, 6, 3, 4, 6, 7, 4, 8,1, 2, 3, 4, 5, 5, 7, 4, 7]

# to use the Line chart, all you need to do is to create an object with the following properties
LineChart = Line(x, y, "Line Chart") # The third property "Line Chart" denotes the chart title

# to show the chart, you just need to call the object's render method.
LineChart.render()
```

After pasting the above example code in your `demo.py` file, all you need to do is run the python code and you should see the output as below:

![Markdown Logo]
(https://github/TunarshBee/sanPlot/public/images/lineChart.png)

##  Available Data Visualization and Their Usage.
The provided documentation defines several visualization for creating different types of plots using sanPlot library in Python. The visualization include:

### _**Line**:_ 
    This visualization creates a line plot with y-axis plotted against the x-axis.

### _**Bar**:_ This visualization creates a bar chart.
### _**Scatter**:_ This visualization creates a scatter plot.
### _**Pie**:_ This visualization creates a pie chart.
### _**Doughnut**:_ This visualization creates a doughnut chart.
### _**Circle_paking_chart**:_ This visualization creates a circular packing visualization.
### _**NetworkViz**:_ This visualization creates a hierarchical network visualization.
