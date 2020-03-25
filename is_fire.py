# is_fire.py
# author: seth briney
# #######################################################
import numpy as np

y=np.load('area.npy')
y=(y>0)*1.0

np.save('is_fire.npy',y)

