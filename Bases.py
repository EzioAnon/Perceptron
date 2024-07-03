import numpy as np
import matplotlib.pyplot as plt



class Base1():
 np.random.seed(0)
 X = np.random.rand(1000, 4) * 10
 y = np.zeros(1000, dtype=int)

 for i, x in enumerate(X):
    if x[0] < 2:
        y[i] = 0  
    elif x[0] < 5:
        y[i] = 1  
    else:
        y[i] = 2  

class Base2():
 np.random.seed(0)
 X = np.random.rand(1000,7) *10
 y = np.zeros(1000, dtype=int)

 for i, x in enumerate(X):
    if np.sin(x[0]) + np.cos(x[1]) < 1:
       y[i] = 0
    elif np.sin(x[2]) + np.cos(x[3]) < 1:
       y[i] = 1
    else:
       y[i] = 2





