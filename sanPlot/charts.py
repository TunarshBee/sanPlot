import matplotlib.pyplot as plt


class Line:
    def __init__(self, 
                x_values,
                y_values, 
                title=None, 
                x_ttl=None, 
                y_ttl=None, 
                color=None, 
                lnStyle=None, 
                marker=None,
                linewidth=None, 
                label=None, 
                cmcStyle=None, 
                graphStyle=None,
                save=None,
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

    def render(self):
        plt.style.use(self.style) if self.style else plt.style.use('seaborn')
        plt.plot(self.x_values, self.y_values, linewidth=self.linewidth, color = self.color, label = self.label, marker = self.marker, linestyle = self.lnstyle)
        plt.xlabel(self.x_ttl) if self.x_ttl else ''
        plt.ylabel(self.y_ttl) if self.y_ttl else ''
        plt.title(self.title) if self.title else ''
        plt.legend(loc='upper left') if self.label else ''
        plt.savefig(self.save) if self.save else ''
        plt.show()


class Bar:
    def __init__(self, x_values, y_values, title=None, x_ttl=None, y_ttl=None):
        self.x_values = x_values
        self.y_values = y_values
        self.title = title
        self.x_ttl = x_ttl
        self.y_ttl = y_ttl

    def render(self):
        plt.bar(self.x_values, self.y_values)
        plt.title(self.title)
        plt.show()


class Scatter:
    def __init__(self, x_values, y_values, title):
        self.x_values = x_values
        self.y_values = y_values
        self.title = title

    def render(self):
        plt.scatter(self.x_values, self.y_values)
        plt.title(self.title)
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
        ax.axis('equal')  # Equal aspect ratio ensures a circular pie
        ax.set_title(self.title)
        plt.show()
