import numpy as np
import pandas as pd
import matplotlib as mlt
from scipy import stats
df_pacientes = pd.read_csv("pacientes.csv")

'''Verique a base pacientes.csv, os dados são ctícios. A sintetiza uma base
de dados de um hospital que trata de pacientes com problemas cardíacos.
Considere a base como a população, portanto as estatísticas da população
são conhecidas. Responda as perguntas abaixo:
3. Considerando uma amostra de 45 números que representam o index do
dataframe, índices= ([909, 751, 402, 400, 726, 39, 184, 269, 255, 769,
209, 715, 677, 381, 793, 697, 89, 280, 232, 756, 358, 36, 439, 768, 967,
699, 473, 222, 89, 639, 883, 558, 757, 84, 907, 895, 217, 224, 311, 348,
146, 505, 273, 957, 362]). Considerando essa amostra é possível dizer
que a idade média das pessoas com problemas cardíacos é maior que
50 anos? Nível de signicância igual a 5%.'''

indices = ([909, 751, 402, 400, 726, 39, 184, 269, 255, 769,
            209, 715, 677, 381, 793, 697, 89, 280, 232, 756,
            358, 36, 439, 768, 967, 699, 473, 222, 89, 639,
            883, 558, 757, 84, 907, 895, 217, 224, 311, 348,
            146, 505, 273, 957, 362])

amostra = df_pacientes.loc[indices, 'Idade']
media_amostra = amostra.mean()
media_populacional_hipotetica = 50
alfa = 0.05
desvio_padrao_populacao = df_pacientes['Idade'].std()
n = len(amostra)

erro_padrao = desvio_padrao_populacao / np.sqrt(n)
z_score = (media_amostra - media_populacional_hipotetica) / erro_padrao
p_valor = 1 - stats.norm.cdf(z_score)

print(f"Média da amostra de idade: {media_amostra:.2f}")
print(f"Média populacional hipotética: {media_populacional_hipotetica}")
print(f"Desvio padrão da população (idade): {desvio_padrao_populacao:.2f}")
print(f"Tamanho da amostra (n): {n}")
print(f"Erro padrão da média: {erro_padrao:.2f}")
print(f"Estatística de teste Z: {z_score:.2f}")
print(f"Valor p: {p_valor:.3f}")
print(f"Nível de significância (alpha): {alfa}")

if p_valor < alfa:
    print("\nRejeitamos a hipótese nula.")
    print("Há evidências estatísticas suficientes para dizer que a idade média das pessoas com problemas cardíacos é maior que 50 anos (com um nível de significância de 5%).")
else:
    print("\nNão rejeitamos a hipótese nula.")
    print("Não há evidências estatísticas suficientes para dizer que a idade média das pessoas com problemas cardíacos é maior que 50 anos (com um nível de significância de 5%).")