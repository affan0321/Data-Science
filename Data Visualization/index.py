import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
print(x)
y = x**2
print(y)

print(plt.plot(x,y))

fig = plt.figure()
axis1 = fig.axes([0.1,0.1,0.8,0.8])
axis1.plot(x,y)