# ========= Imports =======
# Packages
import numpy as np
import plotly.express as px
import pandas as pd
import math

# ========== Declaring Variables ==========
csv_file = './dataframes/csv/OrdersCleanedNew3.csv'

df = pd.read_csv(csv_file)
new_df = pd.DataFrame(columns = ['City', 'Average Time Difference COD False', 'Average Time Difference COD True', 'Difference', 'Orders COD False', 'Orders COD True','Total Orders', 'Winner'])
# ========= Start Program =========
for city in df['City'].unique():
    boolThingy = True
    df_city = df[df['City'] == city]
    df_city = df_city.sort_values(by='Time Difference in Days')
    df_city = df_city.reset_index(drop=True)

    dfIsCODFalse = df_city[df_city['isCOD'] == False]
    dfIsCODTrue = df_city[df_city['isCOD'] == True]

    AverageTimeDifferenceCODFalse = round(dfIsCODFalse['Time Difference in Days'].mean(), 3)
    AverageTimeDifferenceCODTrue = round(dfIsCODTrue['Time Difference in Days'].mean(), 3)

    if math.isnan(AverageTimeDifferenceCODFalse) or math.isnan(AverageTimeDifferenceCODTrue):
        boolThingy = False



    if boolThingy:
        if AverageTimeDifferenceCODFalse < AverageTimeDifferenceCODTrue:
            difference = round(AverageTimeDifferenceCODTrue - AverageTimeDifferenceCODFalse, 3)
            winner = 'At the door!'
        else:
            difference = round(AverageTimeDifferenceCODFalse - AverageTimeDifferenceCODTrue, 3)
            winner = 'Online!'

        # Appending to new dataframe
        new_df = new_df.append({'City': city, 'Average Time Difference COD False': AverageTimeDifferenceCODFalse, 'Average Time Difference COD True': AverageTimeDifferenceCODTrue, 'Difference': difference, 'Orders COD False': len(dfIsCODFalse), 'Orders COD True': len(dfIsCODTrue), 'Total Orders': len(df_city), 'Winner': winner}, ignore_index=True)
new_df = new_df.sort_values(by='Difference', ascending=False)
new_df = new_df.reset_index(drop=True)

# Looking if this data actually is important to compute the average time difference per city

new_df.to_excel('./dataframes/excel/TimeDifferenceRenoDing.xlsx', index=False)