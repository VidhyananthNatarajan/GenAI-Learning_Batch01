import matplotlib.pyplot as plt
import numpy as np

x=np.array([13,46,17,32,84,49,23,67,14,123])
y=np.array([90,78,56,45,23,70,55,10,91,34])

plt.scatter(x,y)
plt.title("Basic Scatter plot for relationship analysis")
plt.xlabel("X-Values")
plt.ylabel("Y-Values")
plt.show()