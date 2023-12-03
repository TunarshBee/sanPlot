import numpy as np
from matplotlib import pyplot as plt

class Pie:
    def __init__(
        self,
        values,
        labels=None,
        title=None,
        colors=None,
        explode=None,
        save_path=None,
    ):
        self.values = values
        self.labels = labels
        self.title = title
        self.colors = colors
        self.explode = explode
        self.save_path = save_path

    def render(self):
        plt.pie(self.values, labels=self.labels, colors=self.colors, explode=self.explode, autopct="%1.1f%%", shadow=True)
        plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(self.title)
        
        if self.save_path:
            plt.savefig(self.save_path)
        
        plt.tight_layout()
        plt.show()



# # Example usage for DoughnutChart
# values = [30, 20, 25, 15, 10]
# labels = ["Label 1", "Label 2", "Label 3", "Label 4", "Label 5"]
# colors = ["#FF9999", "#66B2FF", "#99FF99", "#FFCC99", "#C2C2f2"]
# explode = (0.1, 0, 0, 0, 0)  # Explode the first slice


# # Example usage for PieChart (inherits from DoughnutChart)
# pie_chart = Pie(values, labels=labels, title="Pie Chart Example", colors=colors, explode=explode, save_path="pie_chart.png")
# pie_chart.render()
