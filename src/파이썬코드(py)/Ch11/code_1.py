import matplotlib.pyplot as plt
import random 
import numpy as np

x = [0]
y = [0]
first_run = True
for i in range(1000):
    x = np.append(x,np.array([i]))
    y = np.append(y,np.array(random.uniform(-2,2)))

plt.plot(x,y,marker='o')
plt.axis([0,1000,-3,3])
plt.show()

