import pandas as pd

def direction(x):
    if x == "up":
        return -1
    else:
        return 1


dt = pd.read_csv("2021/2/data.csv", header=None)
# dt = pd.read_csv("2021/2/data_sample.csv", header=None)
dt.columns = ["commands"]

dt[['command', 'amount']] = dt['commands'].str.split(' ', 1, expand=True)
dt["amount"] = pd.to_numeric(dt["amount"])
dt['direction'] = [direction(command) for command in dt["command"]]
dt['amount'] = dt.amount * dt.direction

# ---- part 1 ----
depth = 0
horizontal = 0
for i in range(0, dt.shape[0]):
    if dt["command"][i] == "forward":
        horizontal = horizontal + dt["amount"][i]
    else:
        depth = depth + dt["amount"][i]
    
depth * horizontal

# ---- part 2 ----
aim = 0
depth = 0
horizontal = 0
for i in range(0, dt.shape[0]):
    if dt["command"][i] == "forward":
        horizontal = horizontal + dt["amount"][i]
        depth = depth + aim * dt["amount"][i]
    else:
        aim = aim + dt["amount"][i]
    # print((aim, depth, horizontal))

depth * horizontal
