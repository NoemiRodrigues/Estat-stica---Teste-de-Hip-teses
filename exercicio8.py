import numpy as np
import pandas as pd
import matplotlib as mlt
from scipy import stats
from scipy.stats import chi2_contingency

df_pacientes = pd.read_csv("pacientes.csv")

''' Existe uma associação entre a idade dos pacientes e sua pressão
arterial?
a. Hipótese Nula (H0): se a pressão arterial é independente da idade
b. Hipótese Alternativa (H1): a pressão arterial esta associada a
idade'''

bins_idade = [0, 18, 30, 45, 60, 75, 100]
labels_idade = ['0-17', '18-29', '30-44', '45-59', '60-74', '75+']
df_pacientes['idade_categoria'] = pd.cut(df_pacientes['Idade'], bins=bins_idade, labels=labels_idade, right=False)


bins_pressao = [0, 90, 120, 140, 200]
labels_pressao = ['Baixa', 'Normal', 'Elevada', 'Alta']
df_pacientes['Pressao_Arterial'] = pd.cut(df_pacientes['Pressao_Arterial'], bins=bins_pressao, labels=labels_pressao, right=False)

df_analise = df_pacientes.dropna(subset=['idade_categoria', 'Pressao_Arterial'])

tabela_contingencia = pd.crosstab(df_analise['idade_categoria'], df_analise['Pressao_Arterial'])

print("Tabela de Contingência (Idade vs. Pressão Arterial):\n", tabela_contingencia)

chi2, p_valor, graus_de_liberdade, esperado = chi2_contingency(tabela_contingencia)

alfa = 0.05  

print("\nResultados do Teste Qui-Quadrado:")
print(f"Estatística Qui-Quadrado (χ²): {chi2:.2f}")
print(f"Valor p: {p_valor:.3f}")
print(f"Graus de Liberdade: {graus_de_liberdade}")
print("\nTabela de Frequências Esperadas:\n", pd.DataFrame(esperado, index=tabela_contingencia.index, columns=tabela_contingencia.columns))

if p_valor < alfa:
    print("\nRejeitamos a hipótese nula.")
    print("Há evidências estatísticas suficientes para sugerir uma associação significativa entre a idade e a pressão arterial dos pacientes (com um nível de significância de 5%).")
else:
    print("\nNão rejeitamos a hipótese nula.")
    print("Não há evidências estatísticas suficientes para sugerir uma associação significativa entre a idade e a pressão arterial dos pacientes (com um nível de significância de 5%).")