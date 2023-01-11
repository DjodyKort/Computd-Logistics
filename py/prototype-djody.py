# ======================= Imports =======================
# ===== Local Imports =====
from functions import *

# ===== Packages =====
# Dataframe manipulation
import pandas as pd
import numpy as np
import math
# Machine Learning
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential

# =============== Declaring Variables ===============
# ====== Dataframe cleaning ======
main_df = pd.read_csv('./dataframes/csv/OrdersCleanedNew3.csv')

#  Only importing the important data
temp_df = main_df[['City','State','Quantity','Time Difference in Days','isCOD', 'Date Placed']]

#  Putting and converting the objects to categories in a new dataframe
prediction_df = pd.DataFrame()
prediction_df['City_cat'] = temp_df['City'].astype('category').cat.codes
prediction_df['State_cat'] = temp_df['State'].astype('category').cat.codes
prediction_df['Quantity'] = temp_df['Quantity']
prediction_df['Time Difference in Days'] = temp_df['Time Difference in Days']
prediction_df['Date Placed'] = pd.to_datetime(temp_df['Date Placed'])
prediction_df['isCOD_cat'] = temp_df['isCOD'].astype('category').cat.codes

# Removing every record that has a negative value in State_cat
prediction_df = prediction_df[prediction_df['State_cat'] > 0]
# ====== End Dataframe cleaning ======  

# ====== AI Training ======
# The actual scaler (this is the thing that scales the data)
scaler = MinMaxScaler(feature_range=(0,1)) # range is to scale between 0 and 1
#  Splitting the dataframe into train and test
train_df = prediction_df[:math.floor(len(prediction_df)*0.8)]
test_df = prediction_df[math.floor(len(prediction_df)*0.8):]
# Trains
X_train = []
Y_train = []

#  Splitting the train and test dataframes into X and Y and scaling the things
for i in range(0, len(train_df)):
    X_train.append(scaler.fit_transform(np.array(train_df.iloc[i, :4]).reshape(-1, 1)))
    Y_train.append(scaler.fit_transform(np.array(train_df.iloc[i, 4]).reshape(-1, 1)))

#  Converting the X and Y into numpy arrays
X_train = np.array(X_train)
Y_train = np.array(Y_train)


AIModel = Sequential()
# ====== End AI Training ======
# =============== Start of Program ===============

# =============== Declaring Variables ===============
# ====== Main Dataframe cleaning ======
main_df = pd.read_csv('/content/drive/MyDrive/Google Colab Files/Geleen - Computd - Logistics/dataframes/csv/OrdersCleanedNew3.csv')

#  Only importing the important data
temp_df = main_df[['City','State','Quantity','Time Difference in Days','isCOD', 'Date Placed']]

#  Putting and converting the objects to categories in a new dataframe
prediction_df = pd.DataFrame()
prediction_df['City_cat'] = temp_df['City'].astype('category').cat.codes
prediction_df['State_cat'] = temp_df['State'].astype('category').cat.codes
prediction_df['Quantity'] = temp_df['Quantity']
prediction_df['Time Difference in Days'] = temp_df['Time Difference in Days']
prediction_df['isCOD_cat'] = temp_df['isCOD'].astype('category').cat.codes
prediction_df['Date Placed'] = pd.to_datetime(temp_df['Date Placed'])

# Removing every record that has a negative value in State_cat
prediction_df = prediction_df[prediction_df['State_cat'] > 0]
# ====== End Main Dataframe cleaning ======
print(prediction_df)