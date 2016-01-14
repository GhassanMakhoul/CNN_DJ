import sys
import util
import numpy as np
import pdb
import random


class ConvolutionLayer(HiddenUnit):

	def __init__(self, filters, receptiveField, bias):
		self.filters = filters
		self.receptiveField = receptiveField
		self.bias = bias


	def convolve(self, inputObj, inputResponse):
		"""
		convolve receptive field with input responses (2D kernels) , i.e 
		perform a convolution between contiguous patches of data and weights
		y_ij = x_ij * W_ij (be sure to rotate wieghts twice)
		"""

	def stochasticGDConvolve(self, loss, layer):
		"""
		Return gradient of convolution layer
		"""

	def LayerLabel(self):
		"""
		Return the sting "convolution" to ID layer
		"""

		return "convolution"
