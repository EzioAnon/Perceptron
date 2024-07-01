import numpy as np
import Perceptron

class Validacao_cruzada():
    def __init__(self, K_pastas=10):
        self.K_pastas = K_pastas
        self.X_pastas = None
        self.y_pastas = None
        self.perceptron = Perceptron()
        self.acuracias = []
    
    def divisao(self, X, y):
        classes = np.unique(y)
        numero_classes = len(classes)
        amostras_classes = {c: np.sum(y == c) for c in classes}

        self.X_pastas = [[] for _ in range(self.K_pastas)]
        self.y_pastas = [[] for _ in range(self.K_pastas)]

        for classe_idx, classe_label in enumerate(classes):
            indices_c = np.where(y == classe_label)[0]

            np.random.shuffle(indices_c)

            tamanho_pastas = np.array([len(indices_c) // self.K_pastas] * self.K_pastas)
            tamanho_pastas[:len(indices_c) % self.K_pastas] += 1

            posicao = 0

            for pasta_idx, tamanho in enumerate(tamanho_pastas):
                self.X_pastas[pasta_idx].extend(X[indices_c[posicao:posicao + tamanho]])
                self.y_pastas[pasta_idx].extend(y[indices_c[posicao:posicao + tamanho]])
                posicao += tamanho

        self.X_pastas = [np.array(pasta) for pasta in self.X_pastas]
        self.y_pastas = [np.array(pasta) for self.y_pastas]

    def validacao(self):
        for i in range(self.K_pastas):
            X_validacao = self.X_pastas[i]
            y_validacao = self.y_pastas[i]

            X_treino = np.concatenate([self.X_pastas[j] for j in range(self.K_pastas) if j != i])
            y_treino = np.concatenate([self.y_pastas[j] for j in range(self.K_pastas) if j != i])

            self.perceptron.treinamento(X_treino, y_treino)
            previsao = self.perceptron.previsao(X_validacao)
            self.acuracias.append(self.calculo_acuracia(previsao, y_validacao))

    def calculo_acuracia(self, y_previsao, y_real):
        acertos = np.sum(y_real == y_previsao)
        total = len(y_real)
        acuracia = acertos / total
        return acuracia
    
    def desvio_media(self):
        desvio_padrao = np.std(self.acuracias)
        media = np.mean(self.acuracias)
        return desvio_padrao, media
    
    def melhor_pasta(self):
        melhor_pasta = np.argmax(self.acuracias)
        melhor_acuracia = self.acuracias(melhor_pasta)
        return melhor_pasta, melhor_acuracia