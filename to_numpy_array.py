# analysis1.py

import pandas as pd
import numpy as np

forestfires = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv')

# table = pd.read_csv('forestfires.csv')

# >> table.shape
# (517, 13)

# >> table.columns
# Index(['X', 'Y', 'month', 'day', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain', 'area'],

# >>> table.index
# RangeIndex(start=0, stop=517, step=1)

# >>> table.loc[0]
# X           7
# Y           5
# month     mar
# day       fri
# FFMC     86.2
# DMC      26.2
# DC       94.3
# ISI       5.1
# temp      8.2
# RH         51
# wind      6.7
# rain      0.0
# area      0.0
# Name: 0, dtype: object

# area is area of forest fire, this is the target variable, the variable of interest.

for i in range(12):
    ei = np.zeros((12,))
    ei[i]=1
    exec('e'+str(i+1)+'=ei')

# unique_months = set()
# for month in table['month']:
#     unique_months.add(month)
# print(unique_months)

# {'dec', 'jan', 'mar', 'nov', 'oct', 'feb', 'jun', 'sep', 'aug', 'may', 'apr', 'jul'}
month_to_one_hot_vec = dict({'dec':e12, 'jan':e1, 'mar':e3, 'nov':e11, 'oct':e10, 'feb':e2, 'jun':e6, 'sep':e9, 'aug':e8, 'may':e5, 'apr':e4, 'jul':e7})

months = np.zeros((forestfires.shape[0],12))
for n in range(months.shape[0]):
    months[n,:] = months[n,:]+month_to_one_hot_vec[forestfires['month'][n]]


for i in range(7):
    ei = np.zeros((7,))
    ei[i]=1
    exec('e'+str(i+1)+'=ei')

# unique_days = set()
# for day in table['day']:
#     unique_days.add(day)
# print(unique_days)
# # {'thu', 'mon', 'sun', 'fri', 'tue', 'sat', 'wed'}
day_to_one_hot_vec = dict({'thu':e5, 'mon':e2, 'sun':e1, 'fri':e6, 'tue':e3, 'sat':e7, 'wed':e4})

# 'X', 'Y', 'month', 'day', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain', 'area'

days = np.zeros((forestfires.shape[0],7))
for n in range(days.shape[0]):
    days[n,:] = days[n,:]+day_to_one_hot_vec[forestfires['day'][n]]


feature_data = np.zeros((forestfires.shape[0],forestfires.shape[1]-1+11+6))
feature_data[:,0]=forestfires['X']
feature_data[:,1]=forestfires['Y']
feature_data[:,2]=forestfires['FFMC']
feature_data[:,3]=forestfires['DMC']
feature_data[:,4]=forestfires['DC']
feature_data[:,5]=forestfires['ISI']
feature_data[:,6]=forestfires['temp']
feature_data[:,7]=forestfires['RH']
feature_data[:,8]=forestfires['wind']
feature_data[:,9]=forestfires['rain']
feature_data[:,10:10+7]=days
feature_data[:,10+7:]=months
np.save('archive.ics.uci...forestfires_features.npy',feature_data)

target_data = np.array(forestfires['area']).reshape(-1,1)
np.save('archive.ics.uci...forestfires_area.npy',target_data)

keys = np.array(('X', 'Y', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'))

np.save('archive.ics.uci...forestfires_feature_keys.npy',keys)
