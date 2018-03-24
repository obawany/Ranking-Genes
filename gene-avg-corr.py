import pandas as pd
import os
import logging
import operator
import math

f = open("/Users/obawany/Downloads/GDC_Downloads/PTEN_combined.txt", "r")
g = open("/Users/obawany/Downloads/GDC_Downloads/PTEN_combined..fixed.txt", "w")

g.write("Gene-ensemble \t \taverage_corr \n\n")

for line in f:
	if line[0] == 'E':
		gene_name = line.split("\t")[0]
		# for column in columns:
		average_corr = line.split("\t")[50]
		line = gene_name + "\t" + average_corr
		g.write(line + "\n")
f.close()
g.close()