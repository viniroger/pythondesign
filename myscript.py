#!/usr/bin/env python3
# -*- Coding: UTF-8 -*-

from helpers.inputfiles import InputFiles
from helpers.formulas import Formulas
from helpers.outputfiles import OutputFiles

in_path = '/home/monolito/data'
out_path = '/home/monolito/output'
year = 2012

if_obj = InputFiles(in_path)
df1 = if_obj.read_file('BRB', year)
df2 = if_obj.read_file('SMS', year)

df = Formulas.merge_df(df1, df2)

of_obj = OutputFiles(out_path)
of_obj.scatterplot(df)
