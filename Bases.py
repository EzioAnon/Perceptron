import numpy as np
import matplotlib.pyplot as plt
from Perceptron import Perceptron #Importando meu código






class Base1():
 np.random.seed(0)
 X = np.random.rand(1000, 4) * 10
 y = np.array([1 if x[0] < 5 else -1 for x in X])


#  plt.figure(figsize=(8, 6))
#  plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='red', label='Classe 1')
#  plt.scatter(X[y == -1][:, 0], X[y == -1][:, 1], color='blue', label='Classe -1')
#  plt.xlabel('Feature 1')
#  plt.ylabel('Feature 2')
#  plt.legend()
#  plt.show()
class Base2():
 print()



