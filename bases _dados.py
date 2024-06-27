from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
import numpy as np
import Perceptron # Importando meu código

X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, n_classes=2, class_sep=3.0, random_state=42)


colors = ['red', 'green', 'blue']
plt.figure(figsize=(10, 8))
for class_value in np.unique(y):
    plt.scatter(X[y == class_value][:, 0], X[y == class_value][:, 1], label=f'Class {class_value}', color=colors[class_value])
plt.title('Dados Sintéticos Linearmente Separáveis com Multiclasses')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

X_train,y_train = 0 # Só para para de indicar erro

perceptron = Perceptron()
perceptron.treinamento(X_train,y_train)
y_previsão = [perceptron.previsao(X_test) for X_test in X]
print(y_previsão)