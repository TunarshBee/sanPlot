from matplotlib import pyplot as plt

class Scatter:
    def __init__(
        self,
        x_values,
        y_values,
        title: str,
        x_ttl: str = None,
        y_ttl: str = None,
        color: any = None,
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
        self.logscalex = logscalex
        self.logscaley = logscaley

    def render(self):
        plt.style.use(self.style) if self.style else plt.style.use("seaborn")

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
        colorBar.set_label(self.cbar) if colorBar else ""
        plt.xlabel(self.x_ttl) if self.x_ttl else ""
        plt.ylabel(self.y_ttl) if self.y_ttl else ""
        plt.title(self.title) if self.title else ""
        plt.legend(loc="upper left") if self.label else ""
        plt.savefig(self.save) if self.save else ""
        plt.tight_layout()
        plt.show()
