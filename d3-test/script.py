#! python3
import numpy as np

np.random.seed(50)

file = open('points.json', 'w')

cat = np.random.randn(700, 2) + np.array([0, -3])
mouse = np.random.randn(700, 2) + np.array([3, 3])
dog = np.random.randn(700, 2) + np.array([-3, 3])

feature_set = np.vstack([cat, mouse, dog])

# Create points
file.write('data = [\n')
lastChars = ',\n'

for c, cords in enumerate(feature_set):
    point = {"x": cords[0], "y": cords[1]}

    if c == len(feature_set) - 1:
        lastChars = '\n];'

    file.write('  ' + str(point) + lastChars)
file.close()

print("%s data points created" % len(feature_set))
print("Open index.html to see visualization")
