import numpy as np
import pandas as pd
import matplotlib as mlt
from scipy import stats
from scipy.stats import chi2_contingency

df_pacientes = pd.read_csv("pacientes.csv")

'''7. Lúcia é uma pesquisadora e tem o objetivo de entender a relação de
gênero neste grupo de pacientes. Acredita-se que há uma relação
entre o sexo e condições de saúde adicionais. (Teste qui-quadrado)'''

tabela_contingencia = pd.crosstab(df_pacientes['Genero'], df_pacientes['Nome_Estado_Saude'])

print("Tabela de Contingência (Genero vs. Com condições de saúde adicionais):\n", tabela_contingencia)

chi2, p_valor, graus_de_liberdade, esperado = chi2_contingency(tabela_contingencia)

alfa = 0.05 

print("\nResultados do Teste Qui-Quadrado:")
print(f"Estatística Qui-Quadrado (χ²): {chi2:.2f}")
print(f"Valor p: {p_valor:.3f}")
print(f"Graus de Liberdade: {graus_de_liberdade}")
print("\nTabela de Frequências Esperadas:\n", pd.DataFrame(esperado, index=tabela_contingencia.index, columns=tabela_contingencia.columns))

if p_valor < alfa:
    print("\nRejeitamos a hipótese nula.")
    print("Há evidências estatísticas suficientes para sugerir uma relação significativa entre o sexo e a presença de condições de saúde adicionais neste grupo de pacientes (com um nível de significância de 5%).")
else:
    print("\nNão rejeitamos a hipótese nula.")
    print("Não há evidências estatísticas suficientes para sugerir uma relação significativa entre o sexo e a presença de condições de saúde adicionais neste grupo de pacientes (com um nível de significância de 5%).")