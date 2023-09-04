from adisPlot.charts import Line
import pandas as pd

data =  pd.read_csv("serious-injury-outcome-indicators-2000-2018-CSV.csv")
period = data["Period"]
value = data["Data_value"]

lineChart =  Line(period,value,'serious injury outcome indicators 2000-2018', y_ttl='Period', lnStyle="-", color="orange", marker="o", x_ttl='Data Value', logscaley=True, save="seriousInjuryoutcome.png")
lineChart.render()