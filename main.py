import Bases
import validacao

validacao_cruzada = validacao.Validacao_cruzada()
base_1 = Bases.Base1()
base_2 = Bases.Base2()

validacao_cruzada.divisao(base_1.X,base_1.y)
validacao_cruzada.validacao()
validacao_cruzada.desvio_media()
validacao_cruzada.melhor_pasta()