# ======== Imports ========
# Packages

import pandas as pd
import numpy as np
import plotly.express as px
import math
from sklearn.ensemble import RandomForestRegressor

# ======== Declaring Variables =========
df = pd.read_csv('./dataframes/csv/OrdersCleanedNew3.csv')

# ========= Start Program =========
#print(df)

#drop NANs
# df.dropna(how='all')
#print(df)

# Product Names
#unique_productNames = df['Product Name'].unique()

# States
unique_states = df['State'].unique()

# Printing
#print(f"{unique_productNames}\n\n{unique_states}")

df_pr = df[['City','State','Quantity','Time Difference in Days','isCOD', 'Date Placed']]
#print(df_pr.dtypes)

#first convert the objects to categories 
df_pr['State'] = df_pr['State'].astype('category')
#convert categories to number representations
df_pr['State_cat'] = df_pr['State'].cat.codes

# sort
df_pr = df_pr.sort_values(by=['State_cat'])
df_pr = df_pr[3:]


#first convert the objects to categories 
df_pr['City'] = df_pr['City'].astype('category')
#convert categories to number representations
df_pr['City_cat'] = df_pr['City'].cat.codes

# Deleting the seconds from the "Date Placed" Catogory
df_pr['Date Placed'] = df_pr['Date Placed'].str.slice(0, -3)

#first convert the objects to categories 
df_pr['isCOD'] = df_pr['isCOD'].astype('category')
#convert categories to number representations
df_pr['isCOD_cat'] = df_pr['isCOD'].cat.codes

#convert the date string into datetime format 
df_pr['Date Placed_'] = pd.to_datetime(df_pr['Date Placed'])
    
print(df_pr)

# split the df to train and test 

training_set = df_pr.iloc[:936, [3,6,7]].values 
test_set = df_pr.iloc[936:, [3,6,7]].values 
print(training_set, test_set)

# Feature scaling 
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1)) # range is to scale between 0 and 1
training_set_scaled = scaler.fit_transform(training_set)
# 
#  creating a data structure with 60 time steps (hourly) 
X_train = []
y_train = []

for i in range(60, 936):
  X_train.append(training_set_scaled[i-60:i, 0])
  y_train.append(training_set_scaled[i,0])

X_train, y_train = np.array(X_train), np.array(y_train)

X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
#print(X_train.shape)
#train shape is 876, 60, 1  (876 rows, 60 time steps, 1 feature) which means (values, time steps, features)

# START MODELING
import keras 
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import *
from keras.callbacks import EarlyStopping

# Initializing the LTSM 

model = Sequential()
#Adding the first LSTM layer and some Dropout regularisation
model.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
model.add(Dropout(0.2))
# Adding a second LSTM layer and some Dropout regularisation
model.add(LSTM(units = 50, return_sequences = True))  
model.add(Dropout(0.2))
# Adding a third LSTM layer and some Dropout regularisation
model.add(LSTM(units = 50, return_sequences = True))
model.add(Dropout(0.2))
# Adding a fourth LSTM layer and some Dropout regularisation
model.add(LSTM(units = 50))
model.add(Dropout(0.2))
# Adding the output layer
model.add(Dense(units = 1))

# Compiling the RNN
model.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Fitting the RNN to the Training set
model.fit(X_train, y_train, epochs = 5, batch_size = 32)