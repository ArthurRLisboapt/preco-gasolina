import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


precogasolina_csv = 'gasolina.csv'
dados = pd.read_csv(precogasolina_csv)
dados

plt.figure(figsize=(10, 6))
plt.plot(dados['dia'], dados['venda'], marker='o', linestyle='-', color='b')
plt.title('Vendas de Gasolina por Dia')
plt.xlabel('Dia')
plt.ylabel('Preço de Venda')
plt.savefig('gasolina.png')

versão alterada