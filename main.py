import Bases


base_1 = Bases.Base1()
base_2 = Bases.Base2()
for i in range(k):

 X_train_1,X_teste_1, y_train_1, y_teste_1 = Bases.separacao_dados(base_1.X,base_1.y)
 Bases.treianamento(X_train_1,y_train_1)

