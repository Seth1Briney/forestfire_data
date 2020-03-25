# make_mat.py
# author: seth briney
# #######################################################
'''
This takes a data file
http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv
and from uci, and saves it as a .npy matrix.
'''
import numpy as np
import pandas as pd
forestfires = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv')
month_index = int(np.where( np.array([label for label in forestfires])=='month' )[0])
# it's 2
day_index = int(np.where( np.array([label for label in forestfires])=='day' )[0])
# it's 3
forestfires = np.array(forestfires)

# >>>[thing for thing in forestfires]
# ['X', 'Y', 'month', 'day', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain', 'area']

def month_to_vec(month):
    month = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}[month]
    month_vec = np.zeros([1,12]).reshape(1,-1)
    month_vec[0,month-1] = 1
    return month_vec

def day_to_vec(day):
    day = {'sun':1,'mon':2,'tue':3,'wed':4,'thu':5,'fri':6,'sat':7}[day]
    day_vec = np.zeros([1,7]).reshape(1,-1)
    day_vec[0,day-1] = 1
    return day_vec

output = np.zeros([forestfires.shape[0],forestfires.shape[1]+11+6])

output[:,0:month_index] = forestfires[:,0:month_index]
output[:,day_index+11+6+1:] = forestfires[:,day_index+1:]
output[:,0:2] = forestfires[:,0:2]

for n in range(forestfires.shape[0]):
    output[n,month_index:month_index+11+1] = month_to_vec(forestfires[n,month_index])
    output[n,day_index+11:day_index+11+6+1] = day_to_vec(forestfires[n,day_index])

np.save('ff_mat',output)