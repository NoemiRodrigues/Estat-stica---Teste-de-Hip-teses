import numpy as np
import pandas as pd
import matplotlib as mlt
from scipy import stats
df_pacientes = pd.read_csv("pacientes.csv")

'''4. Queremos entender que tipo de amostra estamos lidando se dividirmos
os conjuntos em 2, sendo um com pessoas que têm condições de
saúde adicionais e o outro com pessoas saudáveis. Seria dependente
ou independente?'''

grupo_com_condicoes = df_pacientes[df_pacientes['Nome_Estado_Saude'] == True]
grupo_saudavel = df_pacientes[df_pacientes['Estado_Saude'] == False]

print("Análise do tipo de amostra:")
print("Ao dividir os pacientes em dois grupos:")
print(f"- Um grupo com pessoas que têm condições de saúde adicionais (tamanho: {len(grupo_com_condicoes)}).")
print(f"- Outro grupo com pessoas consideradas não totalmente saudáveis (tamanho: {len(grupo_saudavel)}).")
print("\nA natureza dessas amostras seria **independente**.")
print("\nJustificativa: ")
print("- Os indivíduos em um grupo são distintos dos indivíduos no outro grupo.")
print("- Não há um pareamento ou correspondência natural entre os membros dos dois grupos.")
print("- A seleção de um paciente para um grupo não influencia diretamente a seleção de um paciente para o outro grupo.")
print("- As medições ou características que poderíamos comparar entre esses grupos seriam obtidas de conjuntos diferentes de pessoas.")

