import numpy as np
from Perceptron import Perceptron

class Validacao_cruzada():
    def __init__(self, K_pastas=10):
        self.K_pastas = K_pastas
        self.X_pastas = None
        self.y_pastas = None
        self.perceptron = Perceptron()
        self.acuracias = []
    
    def divisao(self, X, y):
        classes = np.unique(y)
        

        self.X_pastas = [[] for _ in range(self.K_pastas)]
        self.y_pastas = [[] for _ in range(self.K_pastas)]

        for classe_label in classes:
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
        self.y_pastas = [np.array(pasta) for pasta in self.y_pastas]

    def validacao(self):
        for i in range(self.K_pastas):
            X_validacao = self.X_pastas[i]
            y_validacao = self.y_pastas[i]

            X_treino = np.concatenate([self.X_pastas[j] for j in range(self.K_pastas) if j != i])
            y_treino = np.concatenate([self.y_pastas[j] for j in range(self.K_pastas) if j != i])

            self.perceptron.treinamento(X_treino, y_treino)
            previsao = self.perceptron.previsao(X_validacao)
            acuracia_atual = self.calculo_acuracia(previsao, y_validacao)
            self.acuracias.append(acuracia_atual)
            print(f'Acuracia: {acuracia_atual}')

    def calculo_acuracia(self, y_previsao, y_real):
        acertos = np.sum(y_real == y_previsao)
        total = len(y_real)
        acuracia = acertos / total
        return acuracia
    
    def desvio_media(self):
        desvio_padrao = np.std(self.acuracias)
        media = np.mean(self.acuracias)
        print(f'Desvio Padrão:{desvio_padrao} Média: {media}')
    
    def melhor_pasta(self):
        melhor_pasta = -1
        melhor_acuracia = -1
        melhor_epoca = 1000
        for pasta_idx, acuracia in enumerate(self.acuracias):
            if acuracia > melhor_acuracia:
                melhor_acuracia = acuracia
                melhor_pasta = pasta_idx
                melhor_epoca = self.perceptron.epoca_convergencia[melhor_pasta]
            elif acuracia == melhor_acuracia:
                if self.perceptron.epoca_convergencia[pasta_idx] < melhor_epoca:
                    melhor_pasta = pasta_idx
                    melhor_epoca = self.perceptron.epoca_convergencia[pasta_idx]

        print(f'Melhor Pasta: {melhor_pasta + 1} com Acuracia de: {melhor_acuracia} em: {melhor_epoca} epocas')