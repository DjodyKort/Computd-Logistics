import plotly.express as px
import pandas as pd
# Get csv file
csvDoc = "./csv/TestData.csv"
#variables 
df = pd.read_csv(csvDoc)


# Find correlation between 'Time Difference in Days' and all the other variables and make a line graph out of it
corr = df.corr()
corr = corr['Time Difference in Days']
corr = corr.drop('Time Difference in Days')
corr = corr.sort_values(ascending=False)
print(corr)
fig = px.line(corr, x=corr.index, y=corr.values)
fig.show()
     

