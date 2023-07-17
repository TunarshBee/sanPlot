import matplotlib.pyplot as plt

import bar.Bar


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

    def render(self):
        plt.style.use(self.style) if self.style else plt.style.use("seaborn")
        plt.plot(
            self.x_values,
            self.y_values,
            linewidth=self.linewidth,
            color=self.color,
            label=self.label,
            marker=self.marker,
            linestyle=self.lnstyle if self.lnStyle else None,
        )
        plt.xlabel(self.x_ttl) if self.x_ttl else ""
        plt.ylabel(self.y_ttl) if self.y_ttl else ""
        plt.title(self.title) if self.title else ""
        plt.legend(loc="upper left") if self.label else ""
        plt.savefig(self.save) if self.save else ""
        plt.grid(True) if self.grid else False
        plt.tight_layout()
        plt.show()


class Bar:
    def __init__(
        self,
        x_values,
        y_values,
        title: str = None,
        x_ttl: str = None,
        y_ttl: str = None,
        label: str = None,
        graphStyle: str = None,
        cmcStyle: bool = None,
        color: str = None,
        save: str = None,
        alpha: int = None,
        width: int = None,
        idxwidth: int = None,
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
        self.width = width
        self.alpha = alpha
        self.idxwidth = idxwidth

    def render(self):
        plt.style.use(self.style) if self.style else plt.style.use("seaborn")

        x_indexes = np.arange(len(self.x_values))
        plt.bar(
            x_indexes,
            self.y_values,
            color=self.color if self.color else None,
            alpha=self.alpha if self.alpha else None,
            label=self.label if self.label else None,
        )
        # if plt is more than one,
        # you must specify idxwidth if you are plotting multiple bar charts at once
        plt.bar(
            x_indexes(self.idxwidth),
            self.y_values,
            width=self.width,
            color=self.color,
            alpha=self.alpha,
            label=self.label,
        ) if self.idxwidth else " "
        plt.xticks(ticks=x_indexes, labels=self.x_values)
        plt.xlabel(self.x_ttl) if self.x_ttl else ""
        plt.ylabel(self.y_ttl) if self.y_ttl else ""
        plt.title(self.title) if self.title else ""
        plt.legend(loc="upper left") if self.label else ""
        plt.savefig(self.save) if self.save else ""
        plt.tight_layout()
        plt.show()


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
