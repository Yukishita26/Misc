import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,4))
plt.hlines([0], xmin=[-0.1], xmax=[1.1], color='k')
plt.vlines([0], ymin=[-0.1], ymax=[2.1], color='k')
plt.plot([-0.1,0,1,1,1.1], [0,0,2,0,0], color="r")

n=5000
s=0.2
X = np.random.normal(1,1,n)
Y = np.random.rand(n)*(2*np.exp(-(X-1)**2))
plt.scatter(X[(X<=1)&(Y<=X*2)], Y[(X<=1)&(Y<=X*2)], s=s, c="b")
plt.scatter(X[~((X<=1)&(Y<=X*2))], Y[~((X<=1)&(Y<=X*2))], s=s, c="r")

plt.hlines([2], xmin=[0], xmax=[1], color='k', linestyle='dotted')
#plt.ylim(-1.1,3.1)

plt.show()
