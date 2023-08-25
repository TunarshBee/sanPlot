import matplotlib.pyplot as plt
import networkx as nx
from netgraph import Graph



class NetworkChart:
    def __init__(self, nodes, edges, color, nodes_to_color):
        self.nodes = nodes
        self.edges = edges
        self.color = color
        self.node_to_color = nodes_to_color

    def generate_node_colors(self):
        self.node_color = {
            node: self.color[community_id]
            for node, community_id in self.node_to_color.items()
        }

    def plot(self):
        g = nx.Graph()
        g.add_nodes_from(self.nodes)
        g.add_edges_from(self.edges)

        fig, ax = plt.subplots()

        Graph(
            g,
            node_color=self.node_color,
            node_edge_width=0,
            edge_width=1,
            edge_alpha=1,
            node_layout_kwargs=dict(node_to_community=self.node_to_color),
            node_layout="community",
            edge_layout="bundled",
            ax=ax,
        )
        plt.show()

