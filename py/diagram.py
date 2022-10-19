import plotly.express as px
import pandas as pd
# Get csv file
csvDoc = "./csv/OrdersCleanedNew3.csv"
print(csvDoc, type(csvDoc))
#variables 
df = pd.read_csv(csvDoc)

fig = px.line(df, x="year", y="lifeExp", color='country')
fig.show()

fig = px.bar(df, x="Date Placed", y="Time Difference in Days")
fig.show()