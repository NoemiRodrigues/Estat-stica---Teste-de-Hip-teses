import numpy as np
import pandas as pd
import matplotlib as mlt
from scipy import stats
from scipy.stats import chi2_contingency

df_pacientes = pd.read_csv("pacientes.csv")

'''Qual é o intervalo de confiança para a média da pressão arterial entre
os pacientes com condições de saúde adicionais? (nível de confiança
95%)'''


pacientes_com_condicoes = df_pacientes[df_pacientes['Estado_Saude'] == True]['Pressao_Arterial']

media_amostra = pacientes_com_condicoes.mean()

desvio_padrao_amostra = pacientes_com_condicoes.std(ddof=1)  

n = len(pacientes_com_condicoes)

nivel_confianca = 0.95
alpha = 1 - nivel_confianca

erro_padrao = desvio_padrao_amostra / np.sqrt(n)
graus_de_liberdade = n - 1
t_critico = stats.t.ppf(1 - alpha / 2, graus_de_liberdade)

 
margem_erro = t_critico * erro_padrao

intervalo_confianca_inferior = media_amostra - margem_erro
intervalo_confianca_superior = media_amostra + margem_erro

print(f"Intervalo de Confiança de {nivel_confianca*100}% para a Média da Pressão Arterial (Pacientes com Condições Adicionais):")
print(f"Média da Amostra: {media_amostra:.2f}")
print(f"Desvio Padrão da Amostra: {desvio_padrao_amostra:.2f}")
print(f"Tamanho da Amostra (n): {n}")
print(f"Erro Padrão da Média: {erro_padrao:.2f}")
print(f"Valor t Crítico: {t_critico:.2f}")
print(f"Margem de Erro: {margem_erro:.2f}")
print(f"Intervalo de Confiança: ({intervalo_confianca_inferior:.2f}, {intervalo_confianca_superior:.2f})")