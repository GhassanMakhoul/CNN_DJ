import sys
import util
import numpy as np
import pdb
import random

class AudioDataHandler():

	def __init__(self, rawData, sampling_length):
		self.rawData = rawData
		self.sampleLength - sampling_length

	def convertToSpectroGram(self):
		"""
		Returns spectrogram from raw music file
		"""
