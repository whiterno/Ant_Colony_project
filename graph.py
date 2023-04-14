import matplotlib.pyplot as plt
import numpy as np

data = open("length.txt", "r")
dots = [float(i) for i in data.read().split()]
y = np.array(dots)
plt.plot(y)

plt.show()
