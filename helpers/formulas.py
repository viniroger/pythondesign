#!/usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""
Example of python desing patterns
author: Vinicius Roggério da Rocha
e-mail: viniroger@monolitonimbus.com.br
version: 0.0.1
date: 2019-10-22
"""
import pandas as pd

class Formulas():
	"""
	Create dataframes and do math stuff
	"""

	@staticmethod
	def merge_df(df_left, df_right):
		"""
		Merge two dataframes based on column named "Timestamp"
		:parameter dataframe df_left: input dataframe
		:parameter dataframe df_right: another input dataframe
		"""
		df = pd.merge(df_left, df_right, on='Timestamp')
		return df

