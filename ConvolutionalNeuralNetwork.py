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