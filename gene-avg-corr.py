import pandas as pd
import os
import logging
import operator
import math

f = open("/Users/obawany/Downloads/GDC_Downloads/PTEN_combined.txt", "r")
g = open("/Users/obawany/Downloads/GDC_Downloads/PTEN_combined..fixed.txt", "w")

for line in f:
    if line.strip():
        g.write("\t".join(line.split()[1:]) + "\n")

f.close()
g.close()