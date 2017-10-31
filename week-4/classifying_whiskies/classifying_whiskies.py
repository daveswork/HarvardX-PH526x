import pandas as pd
import numpy as np

#Loading the CSVs
whisky = pd.read_csv("whiskies.txt")

whisky["Region"] = pd.read_csv("regions.txt")


whisky.iloc[0:10]

