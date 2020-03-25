# normalize_mat.py
# author: seth briney
# #######################################################
import numpy as np

X,y = np.load('ff_mat.npy')[:,:-1],np.load('ff_mat.npy')[:,-1]
X = X - np.mean(X,axis=0)
X = X / np.sqrt(np.sum(X**2,axis=0))

np.save('norm_ff_mat.npy',X)
np.save('area',y)