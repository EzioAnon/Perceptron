import numpy as np

def degrau(y):
    return np.where(y >= 1, 1, -1)

class Perceptron:
    def __init__(self, taxa_aprendizado=0.1, epocas=1000):
        self.taxa_aprendizado = taxa_aprendizado
        self.epocas = epocas
        self.pesos = None
        self.bias = 0
        self.epoca_convergencia = []

    def treinamento(self, x, d):
        num_classes = len(np.unique(d))
        dados = x.shape[1]
        self.pesos = np.zeros((num_classes, dados))
        
        for classe in range(num_classes):
            d_classe = np.where(d == classe, 1, -1)
            for epoca in range(self.epocas):
                erro_total = 0
                for idx, x_i in enumerate(x):
                    linear_output = np.dot(x_i, self.pesos[classe]) + self.bias
                    y = degrau(linear_output)
                    erro = d_classe[idx] - y
                    update = self.taxa_aprendizado * erro
                    self.pesos[classe] += update * x_i
                    self.bias += update
                    erro_total += abs(erro)

                if erro_total == 0:
                    self.epoca_convergencia.append(epoca + 1)
                    print(f"Convergiu para classe {classe} em: {epoca + 1} épocas")
                    break

            if erro_total != 0:
                self.epoca_convergencia.append(epoca + 1)
                print(f"Convergiu para classe {classe} em: {epoca + 1} épocas")

    def previsao(self, x):
        linear_outputs = np.dot(x, self.pesos.T) + self.bias
        return np.argmax(linear_outputs, axis=1)
