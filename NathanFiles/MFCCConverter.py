'''
Imports the audio files from music/ directory and converts 
them all into the MFCC representation. Each audio sample is song, 
and is classified according to genre. These will be our training data.
Additionally, a bias term is added, resulting in exactly 312,001 features

The samples are stored in a design matrix musicTrain.

Future: Spectral centers, spectral flatness, echonest features



Notes:
-Used exactly four minutes of each song, zero padded if shorter.
-There are 13 features per increment. Imcrements are a little less than
 one hundreth of a second
-The bias term is 1

'''
# ---------------------------------------------------------------------
# Header and helpers

import numpy as np
import scipy.io.wavfile as wav
from speech_features.features import mfcc
from speech_features.features import logfbank
from os import listdir
from sklearn.preprocessing import normalize


length = 10584000+441 # four minutes at 44100 Hz

def fix_len(n, sig):
	if len(sig) < n:    return np.pad(sig, (0,n-len(sig)), 'constant')
	else:				return sig[:n]

# ---------------------------------------------------------------------
# I/O and data processing

songNames = listdir('music')
songSignals = [wav.read('music/' + song)[1] for song in songNames]
lengthConstant = [fix_len(length, song) for song in songSignals]
mfccs = [mfcc(song, 44100).flatten() for song in lengthConstant]
plusBias = [np.append(song, 1) for song in mfccs]

musicTrain = normalize(np.array(plusBias), axis=0, norm='l2')







