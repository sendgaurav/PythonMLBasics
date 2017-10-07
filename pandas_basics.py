import numpy as np
import pandas as import pd

###############################################################################
### Lesson 3: Manual Data Loading ###
###############################################################################

vals = []

for line in open("data_2d.csv"):
    row = line.split(',')
    sample = map(float, row)
    vals.append(sample)
