""" Find anomalies """


from pathlib import Path
import argparse
import pandas
import matplotlib.pyplot as plt
from scipy.stats import gamma
import numpy as np

from sp_iotsim.fileio import load_data


i = (temp > 19) & (temp < 25)
filtered_temp = temp[i]























if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    p.add_argument("room", help="room to plot")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)
