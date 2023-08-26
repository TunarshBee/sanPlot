import matplotlib.pyplot as plt
import networkx as nx
from netgraph import Graph

class NetworkChart:
    def __init__(self, nodes, edges, color_map, node_color_mapping):
        self.nodes = nodes
        self.edges = edges
        self.color_map = color_map
        self.node_color_mapping = node_color_mapping
        self.generate_node_colors()

    def generate_node_colors(self):
        self.node_color = [self.color_map[self.node_color_mapping[node["id"]]] for node in self.nodes]

    def plot(self):
        g = nx.Graph()
        g.add_nodes_from(node["id"] for node in self.nodes)
        g.add_edges_from((edge["from"], edge["to"]) for edge in self.edges)

        fig, ax = plt.subplots()

        Graph(
            g,
            node_color=self.node_color,
            node_edge_width=0,
            edge_width=1,
            edge_alpha=1,
            ax=ax,
        )
        plt.show()

# Sample data representing relationships between entities
nodes = [
    {"id": 1, "label": "Entity 1"},
    {"id": 2, "label": "Entity 2"},
    {"id": 3, "label": "Entity 3"},
    {"id": 4, "label": "Entity 4"},
    {"id": 5, "label": "Entity 5"}
]

edges = [
    {"from": 1, "to": 2},
    {"from": 1, "to": 3},
    {"from": 2, "to": 3},
    {"from": 4, "to": 5},
    {"from": 4, "to": 1},
    {"from": 5, "to": 3}
]

# Define colors and node-to-color mapping
color_map = {
    0: "red",
    1: "blue",
    2: "green"
}

node_color_mapping = {
    1: 0,
    2: 1,
    3: 1,
    4: 2,
    5: 2
}

# Create a NetworkChart instance and render the network visualization
network_viz = NetworkChart(nodes, edges, color_map, node_color_mapping)
network_viz.plot()
