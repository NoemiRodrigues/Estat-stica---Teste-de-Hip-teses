import numpy as np
import pandas as pd
import matplotlib as mlt
from math import ceil
from scipy.stats import norm

df = pd.read_csv("experimento_teste_ab.csv")
df_pacientes = pd.read_csv("pacientes.csv")

'''2. Calcule qual o tamanho da amostra necessária para o desenvolvimento
de um teste A/B, seguindo os seguintes critérios:
a. O cenário A, da base, como o inicial, que funciona hoje.
b. Considere 95% de conança de que o efeito na conversão não foi
aleatório com um nível de signicância de 5% (alpha = 0,05).
c. Também considere 80% de certeza conseguir capturar o efeito
da nova abordagem.
d. O aumento para 10% de conversão'''

# a. Obter a taxa de conversão do cenário A (base)
taxa_conversao_A = df[df['Versão_Página'] == 'A']['Conversões'].mean()

# d. Definir a taxa de conversão desejada para o cenário B (10% ou 0.1)
taxa_conversao_B = 0.1

# b. Definir o nível de significância (alpha)
alpha = 0.05

# c. Definir o poder estatístico (power)
power = 0.8

# Calcular o valor crítico Z para o nível de significância (alfa/2 para teste bicaudal)
z_alpha_2 = norm.ppf(1 - alpha / 2)

# Calcular o valor crítico Z para o poder estatístico (1 - beta)
beta = 1 - power
z_beta = norm.ppf(1 - beta)

# Calcular o tamanho da amostra necessário por grupo usando a fórmula para proporções
p1 = taxa_conversao_A
p2 = taxa_conversao_B
p_pooled = (p1 * 1 + p2 * 1) / (1 + 1)  # Assumindo tamanhos de amostra iguais (ratio=1)

sample_size = ((z_alpha_2 * np.sqrt(2 * p_pooled * (1 - p_pooled))) +
               (z_beta * np.sqrt(p1 * (1 - p1) + p2 * (1 - p2))))**2 / (p1 - p2)**2

sample_size_per_group = ceil(sample_size)
total_sample_size = 2 * sample_size_per_group


print(f"Taxa de Conversão do Cenário A (Base): {taxa_conversao_A:.4f}")
print(f"Taxa de Conversão Desejada para o Cenário B: {taxa_conversao_B:.2f}")
print(f"Nível de Significância (alpha): {alpha}")
print(f"Poder Estatístico (power): {power}")
print(f"\nTamanho da Amostra Necessária por Grupo (Fórmula): {sample_size_per_group}")
print(f"Tamanho Total da Amostra Necessária (Fórmula): {total_sample_size}")