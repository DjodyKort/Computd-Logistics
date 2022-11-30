# ======== Imports ========
# Packages
import pandas as pd
import numpy 
import plotly.express as px
import math
from sklearn.ensemble import RandomForestRegressor

# ======== Declaring Variables =========
df = pd.read_csv('./dataframes/csv/OrdersCleanedNew3.csv')

# ========= Start Program =========
print(df)
print(numpy.unique(df['Product Name']))

print(df['State'].unique())