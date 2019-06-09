#! python3
import numpy as np

np.random.seed(50)

file = open('points.json', 'w')

cat = np.random.randn(700, 2) + np.array([2, -5])
mouse = np.random.randn(700, 2) + np.array([4, 3])
dog = np.random.randn(700, 2) + np.array([-4, -7])
human = np.random.randn(700, 2) + np.array([-5,8])
bird = np.random.randn(700, 2) + np.array([4, 5])

feature_set = np.vstack([cat, mouse, dog, human, bird])

# Create dots file
file.write('data = [\n')
lastChars = ',\n'

colors = ["green", "blue", "red", "yellow", "cyan"]

for c, coords in enumerate(feature_set):
    if c % 700 == 0:
        color = colors.pop()

    point = {"x": coords[0], "y": coords[1], "color": color}

    if c == len(feature_set) - 1:
        lastChars = '\n];'

    file.write('  ' + str(point) + lastChars)
file.close()

print("%s data points created" % len(feature_set))
print("Open index.html to see visualization")
