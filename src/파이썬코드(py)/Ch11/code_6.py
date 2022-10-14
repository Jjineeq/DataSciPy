import numpy as np
import matplotlib.pyplot as plt

#data = np.random.randn(100)
#data1 = [1, 2, 3, 4, 5]
#data2 = [2, 3, 4, 5, 6]
 
#plt.boxplot([ data1, data2 ] )
#plt.show()

#plt.boxplot(np.array([ data1, data2 ]) )
#plt.show()

k = 0
for i in range(10):
    i = k
    k = np.random.randn(100)

plt.boxplot(np.array([1,2,3,4,5,6,7,8,9,10]))
plt.show()