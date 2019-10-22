#!/usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""
Example of python desing patterns
author: Vinicius Roggério da Rocha
e-mail: viniroger@monolitonimbus.com.br
version: 0.0.1
date: 2019-10-22
"""

class InputFiles():
	"""
	Functions to deal with input files
	"""
	
	def __init__(self, path):
		self.path = path
	
	def read_file(self, place, year):
		"""
		Read CSV file
		:parameter string place: name of place's data
		:parameter int year: year's data
		"""
		import pandas as pd
		filename = '%s/%s_%s.csv' %(self.path, place, year)
		df = pd.read_csv(filename)
		return(df)

