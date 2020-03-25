# covariance.py
# author: seth briney
# #######################################################
import numpy as np
import matplotlib.pyplot as plt

data = np.load('ff_mat.npy')

# >>> np.cov(data.T).shape
# (30, 30) # this is the correct size.

cov_Y = np.cov(data.T)[:-1,-1]

months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','nov','oct','dec']
days = ['mon','tue','wed','thu','fri','sat','sun']
labels = np.array(['X', 'Y']+months+days+['FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain'])

Y = 1/(1+np.exp(-cov_Y))-1/2 # for better visualization
pos_ind = np.where(Y>.1)
neg_ind = np.where(Y<-.1)
plt.bar(labels[pos_ind],Y[pos_ind],color='red')
plt.bar(labels[neg_ind],Y[neg_ind],color='blue')
plt.ylabel('sigmoid cov with area')
plt.title('red increased risk of forest fire, blue decreased risk')
plt.show()

# for n in range(len(cov_Y)):
#     print('cov( area,',labels[n],') =',cov_Y[n])
# cov( area, X ) = 9.335730511447974
# cov( area, Y ) = 3.5131390100910114
# cov( area, jan ) = -0.049795705696250005
# cov( area, feb ) = -0.25474000269893393
# cov( area, mar ) = -0.8885538212406102
# cov( area, apr ) = -0.06900315625327982
# cov( area, may ) = 0.024777937714602783
# cov( area, jun ) = -0.23082163795300892
# cov( area, jul ) = 0.09441211971271311
# cov( area, aug ) = -0.12773593180693513
# cov( area, sep ) = 1.698441403145759
# cov( area, nov ) = -0.18050267644280493
# cov( area, oct ) = -0.02489785284812499
# cov( area, dec ) = 0.00841932436687503
# cov( area, mon ) = -0.5049665632075333
# cov( area, tue ) = -0.4731969247147374
# cov( area, wed ) = -0.027978086155968668
# cov( area, thu ) = -0.22316622434138567
# cov( area, fri ) = 0.4135953173496476
# cov( area, sat ) = -1.249573306044113
# cov( area, sun ) = 2.06528578711409
# cov( area, FFMC ) = 14.098357661223815
# cov( area, DMC ) = 297.59272728022427
# cov( area, DC ) = 779.8034225855785
# cov( area, ISI ) = 2.3966886217444094
# cov( area, temp ) = 36.165676037965014
# cov( area, RH ) = -78.44127232243262
# cov( area, wind ) = 1.4047745003223733
# cov( area, rain ) = -0.13876680461217816