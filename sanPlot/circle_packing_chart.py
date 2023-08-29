import circlify
import matplotlib.pyplot as plt


class Circle_Packing:
    
    def __init__(self, data):
        self.data = data
        self.circles = None

    def compute_circle_positions(self):
        self.circles = circlify.circlify(
            self.data,
            show_enclosure=False,
            target_enclosure=circlify.Circle(x=0, y=0, r=1)
        )

    def render(self):
        fig, ax = plt.subplots(figsize=(10, 19))
        ax.set_title('Repartition of the world population')
        ax.axis('off')

        lim = max(
            max(
                abs(circle.x) + circle.r,
                abs(circle.y) + circle.r,
            )
            for circle in self.circles
        )
        plt.xlim(-lim, lim)
        plt.ylim(-lim, lim)

        for circle in self.circles:
            if circle.level == 2:
                x, y, r = circle
                ax.add_patch(plt.Circle((x, y), r, alpha=0.5, linewidth=2, color="navy"))

        for circle in self.circles:
            if circle.level == 3:
                x, y, r = circle
                label = circle.ex["id"]
                ax.add_patch(plt.Circle((x, y), r, alpha=0.5, linewidth=2, color="#69b3a2"))
                plt.annotate(label, (x, y), ha='center', color="white")

        for circle in self.circles:
            if circle.level == 2:
                x, y, _ = circle
                label = circle.ex["id"]
                plt.annotate(label, (x, y), va='center', ha='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round', pad=.5))

        plt.show()
    def docs(self):
        print(data)
        print("world_population_visualizer = WorldPopulationVisualizer(data)\nworld_population_visualizer.compute_circle_positions()\nworld_population_visualizer.render()")
        
