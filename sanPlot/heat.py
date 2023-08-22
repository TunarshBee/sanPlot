import numpy as np
from matplotlib import pyplot as plt

class Heatmap:
    def __init__(
        self,
        data,
        x_labels=None,
        y_labels=None,
        title=None,
        cmap=None,
        colorbar=False,
        save_path=None,
    ):
        self.data = data
        self.x_labels = x_labels
        self.y_labels = y_labels
        self.title = title
        self.cmap = cmap if cmap else "viridis"
        self.colorbar = colorbar
        self.save_path = save_path

    def render(self):
        plt.imshow(self.data, cmap=self.cmap, aspect="auto")
        if self.colorbar:
            plt.colorbar()
        
        if self.x_labels:
            plt.xticks(np.arange(len(self.x_labels)), self.x_labels)
        if self.y_labels:
            plt.yticks(np.arange(len(self.y_labels)), self.y_labels)
        
        plt.xlabel("X Axis Label")
        plt.ylabel("Y Axis Label")
        plt.title(self.title)
        
        if self.save_path:
            plt.savefig(self.save_path)
        
        plt.tight_layout()
        plt.show()

# Example usage
data = np.random.rand(5, 7)  # Replace this with your own data
x_labels = ["Label 1", "Label 2", "Label 3", "Label 4", "Label 5"]
y_labels = ["Category A", "Category B", "Category C", "Category D", "Category E", "Category F", "Category G"]
heatmap = Heatmap(data, x_labels=x_labels, y_labels=y_labels, title="Custom Heatmap Example", cmap="YlOrRd", colorbar=True, save_path="heatmap.png")
heatmap.render()
