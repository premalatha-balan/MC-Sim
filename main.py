from random import randint
from matplotlib import pyplot as plt
import numpy as np

mini, maxi = input("what is the min and max of throughput?").split(",")
mini = int(mini)
maxi = int(maxi)
print(mini, maxi)
print(maxi-mini)

MC_arr = np.array([randint(mini, maxi) for i in range(100)])
print(MC_arr)
plt.hist(MC_arr)
plt.show()

#e85th = np.percentile(MC_arr, 85)
#print(e85th)

#cMC = np.cumusum(MC_arr)

#e85th = np.percentile(cMC, 85)
#print(cMC)
#print(e85th)

