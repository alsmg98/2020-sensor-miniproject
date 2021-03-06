#!/usr/bin/env python3
"""
This example assumes the JSON data is saved one line per timestamp (message from server).

It shows how to read and process a text file line-by-line in Python, converting JSON fragments
to per-sensor dictionaries indexed by time.
These dictionaries are immediately put into Pandas DataFrames for easier processing.

Feel free to save your data in a better format--I was just showing what one might do quickly.
"""

from pathlib import Path
import argparse
import pandas
import matplotlib.pyplot as plt
from scipy.stats import gamma
import numpy as np

from sp_iotsim.fileio import load_data

data = load_data("dat.txt")

temp = [] 
occu = []

for i,k in temperature.itmes():
    temp.append(list(k.values())[0])
tempDataFrame = pandas.DataFrame(temp)
tempMedian = tempDataFrame.median()
print("Temperature Median:", tempMedian)
tempVariance = tempDataFrame.var()
print("Temperature Variance:", tempVariance)


for i,k in temperature.itmes():
    occu.append(list(k.values())[0])
occuDataFrame = pandas.DataFrame(occu)
occuMedian = tempDataFrame.median()
print("Temperature Median:", occuMedian)
occuVariance = occuDataFrame.var()
print("Temperature Variance:", occuVariance)

if __name__ == "__main__":
    data = load_data("file")
    
    plt.show()

breakpoint()

def plot_time(time: pandas.Series):
    """
    NOTE: in this simulation, time interval is same distribution for all sensors and rooms

    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.fit.html
    """
    
    
    intervals = time.diff().dropna().dt.total_seconds()
    Nbin = 100

    Fa, Floc, Fscale = gamma.fit(intervals)

    ti = np.arange(0.01, 5, 0.01)  # arbitrary time interval range to plot over
    pd = gamma.pdf(ti, Fa, loc=Floc, scale=Fscale)  # fit
    
    ax = plt.figure().gca()
    ax.hist(time.diff().dt.total_seconds(), bins=100)
    ax.set_xlabel("Elapsed Time (seconds)")
    ax.set_title("Time interval")
    ax.set_ylabel("# of occurences")
    ax.grid(True)


def plot_temperature(temp: pandas.Series, name: str):
    """
    Plot temperature for a room
    """

    temp = temp.dropna()
    # get rid of nuisance empty values with .dropna()
    ax = plt.figure().gca()
    temp.hist(ax=ax)
    ax.set_ylabel("# of occurences")
    ax.set_xlabel(r"Temperature [$^\circ$C]")
    ax.set_title(f"{name} temperature")

    ax = plt.figure().gca()
    ax.plot(temp.index, temp.values)
    ax.set_xlabel("time")
    ax.set_ylabel(r"Temperature [$^\circ$C]")
    ax.set_title(f"{name} temperature")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    p.add_argument("room", help="room to plot")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)

    plot_time(data["temperature"].index.to_series())

    plot_temperature(data["temperature"][P.room], P.room)

    plt.show()
