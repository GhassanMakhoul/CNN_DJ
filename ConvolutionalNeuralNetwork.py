import sys
import util
import numpy as np
import pdb
import random


class ConvolutionalNeuralNetwork():

	def __init__(inputObj, weights, biases, layers = 3):
		self.input = inputObj
		self.weights  = weights
		self.bias = biases
		self.layers = layers


	def forwardProp(self):
		""" 
		Pass input looping through layers convolving and poolins as necesary
		outputs a hypothesis which can be tested 
		"""

	def convolve(self, inputObj, inputResponse):
		"""
		convolve receptive field with input responses (2D kernels) , i.e 
		perform a convolution between contiguous patches of data and weights
		y_ij = x_ij * W_ij (be sure to rotate wieghts twice)
		"""

	def maxPooling(self):
		"""
		return maximum of convolution operations
		This effectively downsamples data for next layer 
		"""

	def backPropSGD(self, layer):
		"""
		Given a loss function, compute the gradient of the weignts and adjust as neccesary
		"""

	def LossTwo(self, h_w, y):
		"""
		Return a vector of  squared loss between output hypothesis and the actual data
		"""

	def stochasticGDConvolve(self, loss, layer):
		"""
		Return gradient of convolution layer
		"""
	def stochasticGDMaxPooling(self, loss, layer):
		"""
		Return gradient of max pooling layer: zero everywhere, except argmax of maxPooling
		"""





		