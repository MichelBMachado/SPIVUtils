#-----------------------------------------------------------------------------------
# REQUIRED PACKAGES
#-----------------------------------------------------------------------------------
from keras.utils import Sequence
from numpy import ceil, sqrt

#-----------------------------------------------------------------------------------
# CODE ROUTINES
#-----------------------------------------------------------------------------------
class batch_data(Sequence):
	"""A class to provide a custom keras generator with batching, normalization and velocity scheeme selection"""
	  
	def __init__(self, input, output, batch_size, normalize=True, velocity='Components') :
		"""Future docstring"""
		self.input = input
		self.output = output
		self.batch_size = batch_size
		self.normalize = normalize
		self.velocity = velocity
		self.samples = len(self.input)

	def __len__(self):
		"""Future docstring"""
		return int(ceil(self.samples / self.batch_size))
	
	def normalization(self, holder_x) :
		"""Normalize the images symply dividing the array by 255"""
		batch_x = holder_x/255

		return batch_x
	
	def magnitude(self, holder_y):
		"""Determines the magnitude of the velocity field using its u and v components"""
		u_comp = holder_y[:, 0]
		v_comp = holder_y[:, 1]
		batch_y = sqrt(u_comp ** 2 + v_comp ** 2)

		return batch_y
	
	def __getitem__(self, idx):
		"""Future docstring"""
		holder_x = self.input[idx * self.batch_size : (idx + 1) * self.batch_size]
		holder_y = self.output[idx * self.batch_size : (idx + 1) * self.batch_size]

		if self.normalize == True:
			batch_x = self.normalization(holder_x)

		else:
			batch_x = holder_x

		if self.velocity == 'Magnitude':
			batch_y = self.magnitude(holder_y)

		else:
			batch_y = holder_y

		return (batch_x, batch_y)