from matplotlib import pyplot as plt

class Scatter:
    def __init__(
        self,
        x_values,
        y_values,
        title: str,
        x_ttl: str = None,
        y_ttl: str = None,
        color = None,
        marker: str = None,
        label: str = None,
        cmcStyle: bool = None,
        graphStyle: str = None,
        save: str = None,
        alpha: float = None,
        linewidth: int = None,
        cbar: str = None,
        cmap: str = None,
        size: any = None,
        logscalex: bool = None,
        logscaley: bool = None,
        edgcolor: str = None,
        cName: str = None,
    ):
        self.x_values = x_values
        self.y_values = y_values
        self.title = title
        self.x_ttl = x_ttl
        self.y_ttl = y_ttl
        self.label = label
        self.style = graphStyle
        self.cmcStyle = cmcStyle
        self.color = color
        self.save = save
        self.linewidth = linewidth
        self.marker = marker
        self.alpha = alpha
        self.cbar = cbar
        self.cmap = cmap
        self.size = size
        self.edgcolor = edgcolor
        self.cName = cName
        self.logscalex = logscalex
        self.logscaley = logscaley

    def render(self):
        plt.style.use(self.style) if self.style else plt.style.use("ggplot")
        plt.scatter(
            self.x_values,
            self.y_values,
            s=self.size if self.size else None,
            c=self.color if self.color else None,
            alpha=self.alpha if self.alpha else None,
            linewidth=self.linewidth if self.linewidth else None,
            edgecolor=self.edgcolor if self.edgcolor else None,
            cmap= self.cmap if self.cmap else None,
            marker= self.marker if self.marker else None,
        )
        colorBar = plt.colorbar() if self.cbar else ""
        colorBar.set_label(self.cName) if colorBar else ""
        plt.xscale("log") if self.logscalex else None
        plt.yscale("log") if self.logscaley else None
        plt.xlabel(self.x_ttl) if self.x_ttl else ""
        plt.ylabel(self.y_ttl) if self.y_ttl else ""
        plt.title(self.title) if self.title else ""
        plt.legend(loc="upper left") if self.label else None
        plt.savefig(self.save) if self.save else None
        plt.tight_layout()
        plt.show()

# hours_studied = [3, 2, 5, 4, 6, 5, 7, 6, 8, 7]
# exam_scores = [70, 65, 80, 75, 85, 78, 90, 82, 92, 88]
# # Create a Scatter instance and render the scatter plot

# scatter_plot = Scatter(
# x_values=hours_studied,
# y_values=exam_scores,
# title='Exam Scores vs. Hours Studied',
# x_ttl='Hours Studied',
# y_ttl='Exam Scores',
# color='red',
# marker='x',
# alpha=0.8,
# save='/public/images/scatter_plot.png'
# )
# scatter_plot.render()