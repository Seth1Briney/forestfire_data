import numpy as np
import scipy.stats

# X not to be confused with the 'X' spatial feature which is represented in the first column of X. Confusing, but I like having feature data represented as X.

X = np.load('archive.ics.uci...forestfires_features.npy') 
Y = np.load('archive.ics.uci...forestfires_area.npy')
keys = np.load('archive.ics.uci...forestfires_feature_keys.npy')
# print(keys)
# ['X' 'Y' 'FFMC' 'DMC' 'DC' 'ISI' 'temp' 'RH' 'wind' 'rain' 'sun' 'mon' 'tue' 'wed' 'thu' 'fri' 'sat' 'jan' 'feb' 'mar' 'apr' 'may' 'jun' 'jul' 'aug' 'sep' 'oct' 'nov' 'dec'].

# Spearman's correlation:
# corr_np = np.corrcoef(np.append(X,Y,axis=1).T) # spearman's
# print('corr_np',corr_np.shape)
# (30, 30).

# Spearman's correlation and p-vals:
corr_sp = scipy.stats.spearmanr(np.append(X,Y,axis=1)) # spearman's
# print('corr_sp',np.array(corr_sp).shape)
# (2, 30, 30)
# First entry of corr_sp is corr_np, the Spearman's correlation.
# Second entry is p-vals.


def heat_map():
    import matplotlib.pyplot as plt
    import seaborn as sns; sns.set_theme()

    fig, ax = plt.subplots(ncols=2,nrows=1)

    heat_map = sns.heatmap(np.array(corr_sp)[0,:,:],ax=ax[0])
    heat_map.set_title('Spearman\'s Correlation')
    heat_map2 = sns.heatmap(np.array(corr_sp)[1,:,:],ax=ax[1])
    heat_map2.set_title('p-vals')
    plt.tight_layout()
    plt.show()

def most_statistically_sig():
    # returns rank of most statistically significant as 1, to least statistically significant as 30 corresponding to features in relation to area.
    pvals_area = np.array(corr_sp)[1][-1,:]
    from scipy.stats import rankdata
    return rankdata(pvals_area.reshape(1,-1))


if __name__=='__main__':
    # heat_map()
    sig = most_statistically_sig()
    # print(sig)
# array([ 9., 12., 18.,  6.,  8., 24.,  4., 19., 11.,  7., 27., 30., 15., 23., 21., 17., 26., 10., 28.,  3., 25., 20., 16., 29., 22.,  5., 14., 13.,  2.,  1.])
    keys = np.append(keys,'area')
    corr = np.array(corr_sp)[0][-1,:]
    for n in range(1,30):
        ind = (sig==n)
        print(keys[ind],corr[ind])
        # ['area']
        # ['dec']
        # ['mar']
        # ['temp']
        # ['sep']
        # ['DMC']
        # ['rain']
        # ['DC']
        # ['X']
        # ['jan']
        # ['wind']
        # ['Y']
        # ['nov']
        # ['oct']
        # ['tue']
        # ['jun']
        # ['fri']
        # ['FFMC']
        # ['RH']
        # ['may']
        # ['thu']
        # ['aug']
        # ['wed']
        # ['ISI']
        # ['apr']
        # ['sat']
        # ['sun']
        # ['feb']
        # ['jul']

