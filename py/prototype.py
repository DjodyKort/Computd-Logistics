# ======== Imports ========
# Packages

import pandas as pd
import numpy as np
import plotly.express as px
import math
from sklearn.ensemble import RandomForestRegressor
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import *
from keras.callbacks import EarlyStopping

# ======== Declaring Variables =========
df = pd.read_csv('./dataframes/csv/OrdersCleanedNew3.csv')

# ========= Start Program =========
# States
unique_states = df['State'].unique()

df_pr = df[['City','State','Quantity','Time Difference in Days','isCOD', 'Date Placed']]

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
training_set = df_pr.iloc[:936, [3]].values 
test_set = df_pr.iloc[936:, [3]].values 


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

print(f"X_train.shape: {X_train.shape[1]}")	
# Initializing the LTSM 

model = Sequential()
#Adding the first LSTM layer and some Dropout regularisation
model.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
model.add(Dropout(0.2))
print(f"X_train.shape: {X_train.shape[1]}")
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
model.fit(X_train, y_train, epochs = 1, batch_size = 32)




test_set_scaled = scaler.fit(test_set)
X_test = []
y_test = []
for i in range(60, 462):
    X_test.append(test_set[i-60:i, 0])
    y_test.append(test_set[i, 0])
X_test, y_train = np.array(X_test), np.array(y_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
print(X_test.shape)
# test shape is 402, 60, 1  (402 rows, 60 time steps, 1 feature) which means (values, time steps, features)

# train predict 
trainPredict = model.predict(X_train)
print(trainPredict.shape)
trainPredict = scaler.inverse_transform(trainPredict)

# test predict
testPredict = model.predict(X_test)
testPredict = scaler.inverse_transform(testPredict)


# results 
import math
from sklearn.metrics import mean_squared_error

trainScore = math.sqrt(mean_squared_error(y_train[0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(y_test[0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))






