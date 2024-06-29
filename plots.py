import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table
import Bases
from Perceptron import Perceptron
percptron = Perceptron()
base_1 = Bases.Base1()
base_2 = Bases.Base2()

X_train_1,X_teste_1, y_train_1, y_teste_1 = Bases.separacao_dados(base_1.X,base_1.y)
Bases.treianamento(X_train_1,y_train_1)


df = pd.DataFrame(percptron.historico)


fig, ax = plt.subplots(figsize=(8, 3))


ax.axis('off')


tbl = table(ax, df, loc='center', colWidths=[0.2, 0.2, 0.2,0.2, 0.2, 0.2])


tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1.2, 1.2)


plt.show()