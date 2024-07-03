import matplotlib.pyplot as plt
import numpy as np


def plot_bases(X,y):
 plt.figure(figsize=(8, 6))
 
 for label in np.unique(y):
    plt.scatter(X[y == label][:, 0], X[y == label][:, 1], label=f'Classe {label}')
 
 plt.xlabel('Feature 1')
 plt.ylabel('Feature 2')
 plt.legend()
 plt.show()



#Plot estilo tabela, mas é dificl de armazenar os dados da melhor pasta
# df = pd.DataFrame(percptron.historico)


# fig, ax = plt.subplots(figsize=(8, 3))


# ax.axis('off')


# tbl = table(ax, df, loc='center', colWidths=[0.2, 0.2, 0.2,0.2, 0.2, 0.2])


# tbl.auto_set_font_size(False)
# tbl.set_fontsize(10)
# tbl.scale(1.2, 1.2)


# plt.show()