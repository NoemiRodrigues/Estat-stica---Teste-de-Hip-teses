import numpy as np
import pandas as pd
import matplotlib as mlt
from scipy import stats
df_pacientes = pd.read_csv("pacientes.csv")

'''5. Agora considere o um conjunto de pessoas aleatória que representam
o index do dataframe, índices = ([690, 894, 67, 201, 364, 19, 60, 319,
588, 643, 855, 623, 530, 174, 105, 693, 6, 462, 973, 607, 811, 346, 354,
966, 943, 372]), podemos dizer que a pressão arterial média para
pacientes com condições de saúde adicionais é igual à pressão arterial
média para pacientes sem condições adicionais de saúde? Considere o
nível de signicância a 6%.'''

indices = ([690, 894, 67, 201, 364, 19, 60, 319,
            588, 643, 855, 623, 530, 174, 105, 693, 6, 462, 973, 607, 811, 346, 354,
            966, 943, 372])

amostra_indices = df_pacientes.loc[indices]

grupo_com_condicoes = amostra_indices[amostra_indices['Nome_Estado_Saude'] == True]['Pressao_Arterial']
grupo_sem_condicoes = amostra_indices[amostra_indices['Nome_Estado_Saude'] == False]['Pressao_Arterial']

if len(grupo_com_condicoes) < 2 or len(grupo_sem_condicoes) < 2:
    print("Não há dados suficientes em um ou ambos os grupos para realizar o teste.")
else:
    t_statistic, p_valor = stats.ttest_ind(grupo_com_condicoes, grupo_sem_condicoes, equal_var=False)

    alfa = 0.06

    print(f"Média da pressão arterial (com condições): {grupo_com_condicoes.mean():.2f}")
    print(f"Média da pressão arterial (sem condições): {grupo_sem_condicoes.mean():.2f}")
    print(f"Tamanho da amostra (com condições): {len(grupo_com_condicoes)}")
    print(f"Tamanho da amostra (sem condições): {len(grupo_sem_condicoes)}")
    print(f"Estatística de teste t: {t_statistic:.2f}")
    print(f"Valor p: {p_valor:.3f}")
    print(f"Nível de significância (alpha): {alfa}")

    if p_valor < alfa:
        print("\nRejeitamos a hipótese nula.")
        print("Há evidências estatísticas suficientes para dizer que a pressão arterial média é diferente entre pacientes com e sem condições adicionais de saúde (com um nível de significância de 6%).")
    else:
        print("\nNão rejeitamos a hipótese nula.")
        print("Não há evidências estatísticas suficientes para dizer que a pressão arterial média é diferente entre pacientes com e sem condições adicionais de saúde (com um nível de significância de 6%).")