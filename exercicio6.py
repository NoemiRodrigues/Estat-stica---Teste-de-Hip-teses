import numpy as np
import pandas as pd
import matplotlib as mlt
from scipy import stats
df_pacientes = pd.read_csv("pacientes.csv")

'''6. Existe uma diferença signicativa na pressão arterial média entre
diferentes grupos étnicos nesta população? (Teste ANOVA, alpha é 5%)
a. Hipótese Nula (H0): A pressão arterial média é a mesma em todos
os grupos étnicos.
b. Hipótese Alternativa (H1): Há uma diferença signicativa na
pressão arterial média entre pelo menos dois grupos étnicos
nesta população.'''

grupos_etnicos = df_pacientes['Etnia'].unique()

pressao_por_etnia = []
for etnia in grupos_etnicos:
    pressao = df_pacientes[df_pacientes['Etnia'] == etnia]['Pressao_Arterial']
    pressao_por_etnia.append(pressao)

pressao_por_etnia_filtrada = [p for p in pressao_por_etnia if len(p) >= 2]
grupos_etnicos_filtrados = [grupos_etnicos[i] for i, p in enumerate(pressao_por_etnia) if len(p) >= 2]

if len(pressao_por_etnia_filtrada) < 2:
    print("Não há dados suficientes (pelo menos 2 grupos étnicos com pelo menos 2 amostras cada) para realizar o teste ANOVA.")
else:
    f_statistic, p_valor = stats.f_oneway(*pressao_por_etnia_filtrada)

alfa = 0.05

print("Teste ANOVA para comparar a pressão arterial média entre grupos étnicos:")
print(f"Grupos étnicos considerados: {grupos_etnicos_filtrados}")
print(f"Estatística F: {f_statistic:.2f}")
print(f"Valor p: {p_valor:.3f}")
print(f"Nível de significância (alpha): {alfa}")

if p_valor < alfa:
    print("\nRejeitamos a hipótese nula.")
    print("Há evidências estatísticas suficientes para dizer que existe uma diferença significativa na pressão arterial média entre pelo menos dois grupos étnicos nesta população (com um nível de significância de 5%).")
else:
    print("\nNão rejeitamos a hipótese nula.")
    print("Não há evidências estatísticas suficientes para dizer que a pressão arterial média é a mesma em todos os grupos étnicos (com um nível de significância de 5%).")