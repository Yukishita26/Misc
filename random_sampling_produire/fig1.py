import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,8))
plt.plot(np.linspace(0,1,101), np.linspace(0,1,101)**2, color="r")
plt.plot(np.linspace(1,1.1,11), [1]*11, color="r")
plt.hlines([0], xmin=[-0.1], xmax=[1.1], color='k')
plt.vlines([0], ymin=[-0.1], ymax=[1.1], color='k')


y = np.linspace(0,1,21)
plt.hlines(y, xmin=y*0, xmax=np.sqrt(y), color='gray', linestyle='dashed')
plt.vlines(np.sqrt(y), ymin=y*0, ymax=y, color='gray', linestyle='dashed')

n=2000
s=0.5
Y = np.random.rand(n)
plt.scatter(Y*(-0.1), np.random.rand(n), s=s, c="C0")

x = np.sqrt(Y)
plt.scatter(x, np.random.rand(n)*(-0.1), s=s, c="C0")

plt.vlines([0,1], ymin=[-.65,-.65], ymax=[0,0], color='k', linestyle='dotted')
plt.scatter(x,
            np.random.rand(n)*x*0.5-0.65, s=s, c="C0")

plt.show()
