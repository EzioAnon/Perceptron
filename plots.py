import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

# Exemplo de dados
data = {
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Idade': [25, 30, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba']
}

# Criando um DataFrame
df = pd.DataFrame(data)

# Criando uma figura vazia
fig, ax = plt.subplots(figsize=(8, 3))

# Removendo eixos da figura
ax.axis('off')

# Adicionando uma tabela ao eixo
tbl = table(ax, df, loc='center', colWidths=[0.2, 0.2, 0.2])

# Formatando a tabela
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1.2, 1.2)

# Exibindo a figura
plt.show()
