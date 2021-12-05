import pandas as pd

dt = pd.read_csv("2021/3/data.csv", header=None, names = ["binary"], dtype = {"binary":str})
ncols = len(dt["binary"][0])
bits = dt['binary'].str.split('', ncols, expand=True)[[x for x in range(1, ncols + 1)]]

# ---- part 1 ----
gamma_binary = "".join([n for n in bits.mode().iloc[0]])
gamma_decimal = int(gamma_binary, 2)

def flip(x):
    if str(x) == "1":
        return "0"
    else:
        return "1"

epsilon_binary = "".join([flip(x) for x in str(gamma_binary)])
epsilon_decimal = int(str(epsilon_binary), 2)

gamma_decimal * epsilon_decimal 