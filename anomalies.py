""" Find anomalies """


from pathlib import Path
import argparse
import pandas
import matplotlib.pyplot as plt
from scipy.stats import gamma
import numpy as np

from sp_iotsim.fileio import load_data

std= statistic.pstdev(temp)
print("Standard deviation temperature {:.5}" .format(str(std)))

temp_g = []
temp_b = []

for check in temp:
    if((check-statistic.mean(temp))>=std*3):
        tem_b.append(check)
    else:
        temp_g.append(check)
print("Bad points: ", end="")
for i in tem_b:
    print("{:.5}" .format(float(i)), end="")

print("The standard deviation without bad points: {:.5f}" .format(statistics.pstdev(temp_g)))

print("{}".format(len(temp_b)))
print("{}".format(len(temp_g)))
print("{}".format(len(temp_b)+len(temp_g)))

