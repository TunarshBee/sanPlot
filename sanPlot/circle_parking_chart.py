import circlify
import matplotlib.pyplot as plt

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
            },
            {
                "id": "Europe",
                "datum": 209246682,
                "children": [
                    {"id": "Germany", "datum": 81757600},
                    {"id": "France", "datum": 65447374},
                    {"id": "United Kingdom", "datum": 62041708},
                ],
            },
            {
                "id": "Africa",
                "datum": 311929000,
                "children": [
                    {"id": "Nigeria", "datum": 154729000},
                    {"id": "Ethiopia", "datum": 79221000},
                    {"id": "Egypt", "datum": 77979000},
                ],
            },
            {
                "id": "Asia",
                "datum": 2745929500,
                "children": [
                    {"id": "China", "datum": 1336335000},
                    {"id": "India", "datum": 1178225000},
                    {"id": "Indonesia", "datum": 231369500},
                ],
            },
        ],
    }
]


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

    def plot_network_visualization(self):
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
        print("world_population_visualizer = WorldPopulationVisualizer(data)\nworld_population_visualizer.compute_circle_positions()\nworld_population_visualizer.plot_network_visualization()")
        
        # sanPlot/network_plot.py
circle_packing_chart = Circle_Packing(data)
circle_packing_chart.compute_circle_positions()
circle_packing_chart.plot_network_visualization()