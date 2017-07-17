# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.01)
y = np.sin(x)

plt.plot(x,y)
plt.savefig("test.png")
