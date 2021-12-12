import pandas as pd
import numpy as np

lines = pd.read_table(
    "2021/5/data_sample.csv", header=None, sep=" ", names=["one", "arrow", "two"]
)[["one", "two"]]
lines[["x_one", "y_one"]] = lines["one"].str.split(",", expand=True)
lines[["x_two", "y_two"]] = lines["two"].str.split(",", expand=True)

vertical = lines["x_one"] == lines["x_two"]
horizontal = lines["y_one"] == lines["y_two"]
lines = lines[horizontal | vertical][["x_one", "y_one", "x_two", "y_two"]]

# ---  make grid ---
x_vals = np.array(lines[["x_one", "x_two"]])
y_vals = np.array(lines[["y_one", "y_two"]])
x_names = ["c" + str(x) for x in range(int(np.min(x_vals)), int(np.max(x_vals)) + 1)]
grid_rows = [
    pd.DataFrame(np.repeat(0, [int(np.max(x_vals)) + 1], axis=0).tolist())
    for y in range(int(np.min(y_vals)), int(np.max(y_vals)) + 1)
]

grid_raw = pd.concat(grid_rows, axis=1)
grid_raw.columns = x_names


def ends_to_line(x1, x2, y1, y2):
    # x1, y1, x2, y2 = lines.iloc[1]
    # x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
    # lines.iloc[1]
    is_horizontal = y1 == y2

    if is_horizontal:
        if x1 > x2:
            step = -1
            x2 = x2 - 1
        else:
            step = 1
            x2 = x2 + 1

        xs = [x for x in range(x1, x2, step)]
        ys = np.repeat(y1, len(xs))
        return [(x, y) for x, y in zip(xs, ys)]
    else:
        if y1 > y2:
            step = -1
            y2 = y2 - 1
        else:
            step = 1
            y2 = y2 + 1
        ys = [y for y in range(y1, y2, step)]
        xs = np.repeat(x1, len(ys))
        return [(x, y) for x, y in zip(xs, ys)]


grid = grid_raw.copy()

for i in range(0, lines.shape[0]):
    # i = 1
    # lines.iloc[i]
    line = ends_to_line(
        int(lines.iloc[i][0]),
        int(lines.iloc[i][2]),
        int(lines.iloc[i][1]),
        int(lines.iloc[i][3]),
    )

    # grid = grid_raw.copy()
    for coords in line:
        grid.iloc[coords[1], coords[0]] = grid.iloc[coords[1], coords[0]] + 1

    print(i)
    print(grid)

len(np.where(np.array(grid) >= 2)[0])
