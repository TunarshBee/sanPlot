from matplotlib import pyplot as plt
class Line:
    def __init__(
        self,
        x_values,
        y_values,
        title: str = None,
        x_ttl: str = None,
        y_ttl: str = None,
        color: str = None,
        lnStyle: str = None,
        marker: str = None,
        linewidth: str = None,
        label: str = None,
        logscaley: bool = None,
        logscalex: bool = None,
        cmcStyle: bool = None,
        graphStyle: str = None,
        save: str = None,
        grid: bool = None,
    ):
        self.x_values = x_values
        self.y_values = y_values
        self.title = title
        self.x_ttl = x_ttl
        self.y_ttl = y_ttl
        self.marker = marker
        self.label = label
        self.style = graphStyle
        self.cmcStyle = cmcStyle
        self.color = color
        self.linewidth = linewidth
        self.lnStyle = lnStyle
        self.save = save
        self.grid = grid
        self.logscaley = logscaley
        self.logscalex = logscalex

    def render(self):
        plt.style.use(self.style) if self.style else plt.style.use("seaborn")
        plt.plot(
            self.x_values,
            self.y_values,
            linewidth=self.linewidth,
            color=self.color,
            label=self.label,
            marker=self.marker,
            linestyle=self.lnStyle if self.lnStyle else None,
        )
        plt.xlabel(self.x_ttl) if self.x_ttl else ""
        plt.ylabel(self.y_ttl) if self.y_ttl else ""
        plt.xscale("log") if self.logscalex else None
        plt.yscale("log") if self.logscaley else None
        plt.title(self.title) if self.title else ""
        plt.legend(loc="upper left") if self.label else ""
        plt.savefig(self.save) if self.save else ""
        plt.grid(True) if self.grid else False
        plt.tight_layout()
        plt.show()

