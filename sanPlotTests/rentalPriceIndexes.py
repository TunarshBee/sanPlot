from sanPlot.charts import Bar
import pandas as pd

data =  pd.read_csv("rental-price-indexes-jan-2022(1.5 years).csv")
period = data["TIME_REF"]
value = data["DATA_VAL"]


barChart =  Bar(period,value,'Rental Price Indexes July 2020- Jan2022', y_ttl='Time Reference', x_ttl='Data Value', color="teal", graphStyle="ggplot",save="rentalPriceIndex.png")
barChart.render()