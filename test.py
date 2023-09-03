# Test for Bar chart
def test_bar_chart():
    x_values = ['A', 'B', 'C', 'D']
    y_values = [10, 20, 15, 30]
    
    bar_chart = Bar(
        x_values=x_values,
        y_values=y_values,
        title="Bar Chart Example",
        x_ttl="X Axis Label",
        y_ttl="Y Axis Label",
        label="Data Label",
        color="blue",
        save="bar_chart.png"
    )
    bar_chart.render()

# Test for Line chart
def test_line_chart():
    x_values = [1, 2, 3, 4, 5]
    y_values = [10, 15, 20, 25, 30]
    
    line_chart = Line(
        x_values=x_values,
        y_values=y_values,
        title="Line Chart Example",
        x_ttl="X Axis Label",
        y_ttl="Y Axis Label",
        color="green",
        marker="o",
        linewidth=2,
        label="Data Label",
        grid=True,
        save="line_chart.png"
    )
    line_chart.render()

# Test for Scatter chart
def test_scatter_chart():
    x_values = [1, 2, 3, 4, 5]
    y_values = [10, 15, 20, 25, 30]
    
    scatter_chart = Scatter(
        x_values=x_values,
        y_values=y_values,
        title="Scatter Chart Example",
        x_ttl="X Axis Label",
        y_ttl="Y Axis Label",
        color="red",
        marker="o",
        alpha=0.7,
        size=100,
        cbar="Color Bar",
        cmap="viridis",
        logscalex=True,
        logscaley=True,
        edgcolor="black",
        save="scatter_chart.png"
    )
    scatter_chart.render()

# Test for Circle Packing chart
def test_circle_packing_chart():
    circle_packing = Circle_Packing(data)
    circle_packing.compute_circle_positions()
    circle_packing.plot_network_visualization()

# Test for NetworkChart (adisPlot/network_plot.py)
def test_network_chart():
    nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    edges = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 7), (6, 8), (6, 9), (6, 10), (7, 8), (7, 9), (7, 10), (8, 9), (8, 10), (9, 10)]
    color = ["red", "blue", "green"]
    nodes_to_color = {0: 2, 1: 0, 2: 1, 3: 1, 4: 0, 5: 0, 6: 1, 7: 2, 8: 2, 9: 2, 10: 1}
    
    network_chart = NetworkChart(
        nodes=nodes,
        edges=edges,
        color=color,
        nodes_to_color=nodes_to_color
    )
    network_chart.generate_node_colors()
    network_chart.render()

# Test for Pie chart
def test_pie_chart():
    labels = ['Category A', 'Category B', 'Category C']
    sizes = [30, 40, 30]
    
    pie_chart = Pie(
        labels=labels,
        sizes=sizes,
        title="Pie Chart Example"
    )
    pie_chart.render()

# Run the tests
if __name__ == "__main__":
    test_bar_chart()
    test_line_chart()
    test_scatter_chart()
    test_circle_packing_chart()
    test_network_chart()
    test_pie_chart()
