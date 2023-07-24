import matplotlib.pyplot as plt

from .bar import Bar
from .networkViz import NetworkChart
from .line import Line
from .circle_packing_chart import Circle_Packing
from .scatter import Scatter

class Pie:
    def __init__(self, labels, sizes, title):
        self.labels = labels
        self.sizes = sizes
        self.title = title

    def render(self):
        plt.pie(self.sizes, labels=self.labels)
        plt.title(self.title)
        plt.show()


class Doughnut:
    def __init__(self, labels, sizes, title):
        self.labels = labels
        self.sizes = sizes
        self.title = title

    def render(self):
        fig, ax = plt.subplots()
        ax.pie(self.sizes, labels=self.labels)
        ax.axis("equal")  # Equal aspect ratio ensures a circular pie
        ax.set_title(self.title)
        plt.show()
