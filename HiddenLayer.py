import sys
import util
import numpy as np
import pdb
import random


class HiddenLayer():

	def __init__(label, weights):
		self.label = label
		self.weights = weights

	def sigmoidalActivation(self, weights, input):
		"""
		Return the result of the dot product between the weights and the input
		 fed into the  sifgmoidal exponential activation function  
		"""

	def softmaxActivation(self, weighs, input):
		"""
		Return the result of the dot product between the weights and the input
		 fed into the  softmax exponential activation function. 
		 Normally used at the last layer. 
		"""