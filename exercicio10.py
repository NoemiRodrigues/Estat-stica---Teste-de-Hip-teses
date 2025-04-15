import numpy as np
import pandas as pd
import matplotlib as mlt
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df_pacientes = pd.read_csv("pacientes.csv")

'''10. A distribuição da pressão arterial na população segue uma distribuição
normal?
a. Hipótese Nula (H0): A distribuição da pressão arterial na
população segue uma distribuição normal.
b. Hipótese Alternativa (H1): A distribuição da pressão arterial na
população não segue uma distribuição normal.'''


shapiro_statistic, shapiro_p_valor = stats.shapiro(df_pacientes['Pressao_Arterial'])

alpha = 0.05  

print("Teste de Shapiro-Wilk para Normalidade da Pressão Arterial:")
print(f"Estatística de Teste (W): {shapiro_statistic:.3f}")
print(f"Valor p: {shapiro_p_valor:.3f}")
print(f"Nível de Significância (alpha): {alpha}")

if shapiro_p_valor > alpha:
    print("\nNão rejeitamos a hipótese nula.")
    print("Os dados da pressão arterial parecem seguir uma distribuição normal (com um nível de significância de 5%).")
else:
    print("\nRejeitamos a hipótese nula.")
    print("Os dados da pressão arterial não parecem seguir uma distribuição normal (com um nível de significância de 5%).")


