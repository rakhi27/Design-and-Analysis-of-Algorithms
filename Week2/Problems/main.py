import numpy as np
import time
import matplotlib.pyplot as plt


def fastPower(a,b) :
  if b == 1:
    return a
  else:
    c = a*a
    ans = fastPower(c,np.floor(b/2))
  if (b%2 != 0):
    return a*ans
  else: return ans

timeArray = np.array([],dtype='float')

bArray = np.arange(1000, dtype='float')

for b in range (1,1001):
    t0 = time.time()
    fastPower(3,b)
    t1 = time.time()
    timeArray = np.append(timeArray, float(t1-t0))

plt.plot(bArray, timeArray)

plt.show()


