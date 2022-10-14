import matplotlib.pyplot as plt 
import numpy as np 
 
xData = np.random.randn(10000)
yData = np.random.randn(10000)   

plt.scatter(xData, yData, alpha = 0.2) 
plt.title('Random Position') 
plt.xlabel('x') 
plt.ylabel('y') 
 
#plt.savefig("age.png", dpi=600)
plt.show()