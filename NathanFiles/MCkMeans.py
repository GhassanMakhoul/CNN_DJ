'''
Runs k-Means on the set of feature vectors returned by MFCCConverter


Future: Neural Gas?
'''

from MFCCConverter import musicTrain
from scipy.cluster.vq import kmeans2

print('Running kmeans')
means, labels = kmeans2(musicTrain, 2)
