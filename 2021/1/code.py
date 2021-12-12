# count the number of times a depth measurement increases from the previous measurement.

import pandas as pd

dt = pd.read_csv("2021/1/data.csv", header=None)
dt.columns = ["depth"]

#  ---- part 1 ----
def diff(x, x_ahead):
    if (x_ahead - x) > 0:
        return 1
    else:
        return 0


# https://stackoverflow.com/a/48519175/3362993
dt["diff"] = dt["depth"].rolling(window=2).apply(lambda x: diff(x.iloc[0], x.iloc[1]))
dt["diff"].sum(skipna=True)

# ---- part 2 ----
dt["sum_3"] = dt["depth"].rolling(window=3).apply(lambda x: sum(x))
dt["diff_3"] = dt["sum_3"].rolling(window=2).apply(lambda x: diff(x.iloc[0], x.iloc[1]))
dt["diff_3"].sum(skipna=True)
