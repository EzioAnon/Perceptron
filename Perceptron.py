import numpy as np
import pandas as pd

def degrau(y):
    return +1 if y >= 0 else -1

class Perceptron:
    def __init__(self,):
        self.taxa_aprendizado = 0.1
        self.epocas = 1000
        self.pesos = None
        self.bias = 0
        self.historico = pd.DataFrame(columns=['Época', 'Peso 1', 'Peso 2', 'Peso 3', 'Bias', 'Erro'])

    def treinamento(self, x, d):
        dados = x.shape[1]
        self.pesos = np.zeros(dados)

        for _ in range(self.epocas):
            epoca = 0
            for idx, x_i in enumerate(x):
                linear_output = np.dot(x_i,self.pesos) + self.bias
                y = degrau(linear_output)
                erro  = d[idx] - y
                update = self.taxa_aprendizado * erro
                self.pesos += update * x_i
                self.bias += update
                nova_linha = {
                    'Época': epoca,
                    'Peso 1': self.pesos[0],
                    'Peso 2': self.pesos[1],
                    'Peso 3': self.pesos[2],
                    'Bias': self.bias,
                    'Erro': erro
                }

                if update != 0:
                    epoca += 1
                    # print(f'Época {epoca}')
                    # print('Pesos: ',self.pesos)
                    # print('Bias: ',self.bias)

            
            
            if erro == 0:
                print(f"Convergiu em: {epoca} épocas ")
                break
    def previsao(self,x):
        linear_output = np.dot(x,self.pesos) + self.bias
        return degrau(linear_output)