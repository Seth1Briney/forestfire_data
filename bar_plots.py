import numpy as np
import scipy.stats

# X not to be confused with the 'X' spatial feature which is represented in the first column of X. Confusing, but I like having feature data represented as X.

X = np.load('archive.ics.uci...forestfires_features.npy') 
Y = np.load('archive.ics.uci...forestfires_area.npy')
keys = np.load('archive.ics.uci...forestfires_feature_keys.npy')
# print(keys)
# ['X' 'Y' 'FFMC' 'DMC' 'DC' 'ISI' 'temp' 'RH' 'wind' 'rain' 'sun' 'mon' 'tue' 'wed' 'thu' 'fri' 'sat' 'jan' 'feb' 'mar' 'apr' 'may' 'jun' 'jul' 'aug' 'sep' 'oct' 'nov' 'dec'].

# Spearman's correlation and p-vals:
corr_sp = scipy.stats.spearmanr(np.append(X,Y,axis=1)) # spearman's
# print('corr_sp',np.array(corr_sp).shape)
# (2, 30, 30)
# First entry of corr_sp is corr_np, the Spearman's correlation.
# Second entry is p-vals.

def most_statistically_sig():
    # returns rank of most statistically significant as 1, to least statistically significant as 30 corresponding to features in relation to area.
    pvals_area = np.array(corr_sp)[1][-1,:]
    from scipy.stats import rankdata
    return rankdata(pvals_area.reshape(1,-1))

def bar_plots():

    import matplotlib.pyplot as plt
    global keys
    xlabels = keys.reshape(-1,).tolist()
    for n in range(len(xlabels)):
        xlabels[n] = xlabels[n]+'\n'*(n%2)
    print(xlabels)
    corr = np.array(corr_sp)[0][-1,:-1]
    pval = np.array(corr_sp)[1][-1,:-1]

    fig, axs = plt.subplots(1, 2)

    axs[0].set_title('Spearman\'s Correlation')
    axs[0].bar(keys,corr)
    axs[0].set_xticks([n for n in range(len(xlabels))])
    axs[0].set_xticklabels(xlabels)
    axs[1].set_title('Pvals')
    axs[1].bar(keys,pval)
    axs[1].set_xticks([n for n in range(len(xlabels))])
    axs[1].set_xticklabels(xlabels)
    for tick in axs[0].xaxis.get_major_ticks()[1::2]:
        tick.set_pad(15)
    for tick in axs[1].xaxis.get_major_ticks()[1::2]:
        tick.set_pad(15)

    plt.tight_layout()
    plt.show()
    plt.subplots(1, 2, sharey='row')

if __name__=='__main__':
    bar_plots()
    # sig = most_statistically_sig()
    # keys = np.append(keys,'area')
    # corr = np.array(corr_sp)[0][-1,:]
    # for n in range(1,30):
    #     ind = (sig==n)
    #     print(keys[ind],corr[ind])
