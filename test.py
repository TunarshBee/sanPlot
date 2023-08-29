from sanPlot.networkViz import NetworkChart



nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
edges = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 7), (6, 8), (6, 9), (6, 10), (7, 8), (7, 9), (7, 10), (8, 9), (8, 10), (9, 10)]
color = ["red", "blue", "green"]
nodes_to_color = {0: 2, 1: 0, 2: 1, 3: 1, 4: 0, 5: 0, 6: 1, 7: 2, 8: 2, 9: 2, 10: 1}


# Create a NetworkChart instance and render the network visualization
network_chart = NetworkChart(nodes, edges, color, nodes_to_color)

# Generate node colors based on community mapping and plot at last
network_chart.generate_node_colors()  
network_chart.plot()