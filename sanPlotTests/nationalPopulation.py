import pandas as pd
from sanPlot.charts import Scatter


data = pd.read_csv("national-population.csv")
period=data["period"]
migration = data["net_migration"]



scatterChar = Scatter(migration, period, 'national-population', x_ttl='Period', color="green", marker="X", y_ttl="Net Migration", save="nationalPopulation.png", alpha=0.8)
scatterChar.render()