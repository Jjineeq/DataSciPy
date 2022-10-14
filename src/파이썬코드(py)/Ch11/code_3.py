import math
from turtle import color 
import matplotlib.pyplot as plt 
 
x = [] 
y = [] 
z = [] 

for angle in range(360): 
    x.append(angle) 
    y.append(math.sin(math.radians(angle))) 
    z.append(math.cos(math.radians(angle)))
 
plt.plot(x, y)
plt.plot(x, z, color = 'r')
plt.title("SIN, COS WAVE") 
plt.show()