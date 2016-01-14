import sys
import util
import numpy as np
import pdb
import random

class PoolingLayer(HiddenLayer):

	def __init__(self, **args):

		self.stuff = args[0]

	def maxPooling(self):
		"""
		return maximum of convolution operations
		This effectively downsamples data for next layer 
		"""
	def stochasticGDMaxPooling(self, loss, layer):
		"""
		Return gradient of max pooling layer: zero everywhere, except argmax of maxPooling
		"""


