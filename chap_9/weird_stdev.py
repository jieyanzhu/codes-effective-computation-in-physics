from statistics import stdev
import numpy as np

print(stdev([0,4,8,12]))

print(stdev(np.array([0, 4, 8, 12])))

print(np.sqrt(80/3))

# This is because the type of numbers in np.array([0, 4, 8, 12]) is `int` rather than `float64`.
print(stdev(np.array([0, 4, 8, 12], dtype=float)))
