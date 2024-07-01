import numpy as np

class Validacao_cruzada():
    def __init__(self,K_pastas):
        self.K_pastas = K_pastas
        self.X_pastas = None
        self.y_pastas = None
    
    def divisao(self,X,y):
        classes = np.unique(y)
        numero_classes = len(classes)
        amostras_classes = {c : np.sum(y==c) for c in classes}

        self.X_pastas = [[]for _ in range(self.K_pastas)]
        self.y_pastas = [[]for _ in range(self.K_pastas)]

        for classe_idx, classe_label in enumerate(classes):
            indices_c = np.where(y==c)[0]

            np.random.shuffle(indices_c)   

            tamanho_pastas = np.array([len(indices_c)// self.K_pastas] * self.K_pastas)
            tamanho_pastas[:len(indices_c) % self.K_pastas] += 1

            posicao = 0 

            for pasta_idx, tamanho in enumerate(tamanho_pastas):
                self.X_pastas[pasta_idx].extend(X[indices_c[posicao:posicao + tamanho]])
                self.y_pastas[pasta_idx].extend(y[indices_c[posicao:posicao + tamanho]])
                posicao += tamanho

        self.X_pastas = [np.array(pasta) for pasta in self.X_pastas]
        self.y_pastas = [np.array(pasta) for pasta in self.y_pastas]

        return self.X_pastas, self.y_pastas                         