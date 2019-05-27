#! python3
import numpy as np
import json

np.random.seed(50)

points = np.random.randn(700, 2) + np.array([0, -3])

data = {}

for p, cord in enumerate(points):
    position = { "x": cord[0], "y": cord[1] }
    data.setdefault("p" + str(p), position)

with open("points.json", "w") as data_file:
    json.dump(data, data_file, indent=2)

print("%s data points created" % (p+1))
print("Open index.html to see visualization")
