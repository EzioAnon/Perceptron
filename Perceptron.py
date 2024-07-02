import numpy as np
import pandas as pd

def degrau(y):
    return np.where(y >= 1, 1, -1)

class Perceptron:
    def __init__(self,):
        self.taxa_aprendizado = 0.1
        self.epocas = 1000
        self.pesos = None
        self.bias = 0
        self.epoca_convergencia = []
        

    def treinamento(self, x, d):
        dados = x.shape[1]
        self.pesos = np.zeros(dados)

        for epoca in range(self.epocas):
            erro_total = 0
            for idx, x_i in enumerate(x):
                linear_output = np.dot(x_i,self.pesos) + self.bias
                y = degrau(linear_output)
                erro  = d[idx] - y
                update = self.taxa_aprendizado * erro
                self.pesos += update * x_i
                self.bias += update
                erro_total += abs(erro) 
                 
                
                
                    
            # print(f'Época {epoca + 1}')
            # print('Pesos: ',self.pesos)
            # print('Bias: ',self.bias)

            
            
            if erro_total == 0:
                self.epoca_convergencia.append(epoca + 1)
                print(f"Convergiu em: {epoca + 1} épocas ")
                break
        if erro_total !=0:
            self.epoca_convergencia.append(epoca + 1)
            print(f"Convergiu em: {epoca + 1 } épocas ")
    
    def previsao(self,x):
        linear_output = np.dot(x,self.pesos) + self.bias
        return degrau(linear_output)
