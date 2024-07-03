import Bases
import validacao
from plots import plot_bases
from plots import reta_2d

validacao_cruzada = validacao.Validacao_cruzada()

base_1 = Bases.Base1()
base_2 = Bases.Base2()

plot_bases(base_1.X,base_1.y)
# validacao_cruzada.divisao(base_1.X,base_1.y)
# validacao_cruzada.validacao()
# validacao_cruzada.desvio_media()
# validacao_cruzada.melhor_pasta()
# retas_1 = reta_2d(validacao_cruzada.melhor_peso,validacao_cruzada.melhor_bias)
# plot_bases(base_1.X,base_1.y,retas_1)


# plot_bases(base_2.X,base_2.y)
# validacao_cruzada.divisao(base_2.X,base_2.y)
# validacao_cruzada.validacao()
# validacao_cruzada.desvio_media()
# validacao_cruzada.melhor_pasta()
# retas_2 = reta_2d(validacao_cruzada.melhor_peso,validacao_cruzada.melhor_bias)
# plot_bases(base_1.X,base_1.y,retas_2)
