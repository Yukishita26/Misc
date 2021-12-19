import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,8))
plt.hlines([0], xmin=[-0.1], xmax=[1.1], color='k')
plt.vlines([0], ymin=[-0.1], ymax=[2.1], color='k')
plt.plot([-0.1,0,1,1,1.1], [0,0,2,0,0], color="r")

n=5000
s=0.5
X = np.random.rand(n)
Y = np.random.rand(n)*2
plt.scatter(X[Y<=X*2], Y[Y<=X*2], s=s, c="b")
plt.scatter(X[Y>X*2], Y[Y>X*2], s=s, c="r")

plt.hlines([2], xmin=[0], xmax=[1], color='k', linestyle='dotted')

plt.show()
