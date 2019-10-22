#!/usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""
Example of python desing patterns
author: Vinicius Roggério da Rocha
e-mail: viniroger@monolitonimbus.com.br
version: 0.0.1
date: 2019-10-22
"""

class OutputFiles():
	"""
	Functions to deal with output files
	"""
	
	def __init__(self, path):
		self.path = path
	
	def scatterplot(self, df):
		"""
		Scatterplot from a given dataframe and save to file
		:parameter dataframe df: input dataframe
		"""
		import matplotlib.pyplot as plt
		plt.plot(df['var1'], df['var2'], '.')
		plt.show()
		return()
