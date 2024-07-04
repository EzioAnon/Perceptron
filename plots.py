import matplotlib.pyplot as plt
import numpy as np


def plot_bases(X,y, retas=None):
 plt.figure(figsize=(8, 6))
 
 for label in np.unique(y):
    plt.scatter(X[y == label][:, 0], X[y == label][:, 1], label=f'Classe {label}')
   
 if retas:
   x_min, x_max = plt.xlim()
   for i,(a,b) in enumerate(retas):
     x_vals = np.array([x_min, x_max])
     y_vals = a * x_vals + b
     plt.plot(x_vals,y_vals, label=f'Reta{i + 1}', linestyle='--')

 
 plt.legend()
 plt.show()

def reta_2d(melhor_peso, melhor_bias , indices = [0,1]):
  pesos_2d = melhor_peso[:, indices]
  retas = []

  for peso in pesos_2d:
    a = -peso[0]/peso[1]
    b = -melhor_bias/peso[1]
    retas.append((a,b))

  return retas








