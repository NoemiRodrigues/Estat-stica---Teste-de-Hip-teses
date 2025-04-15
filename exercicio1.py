import numpy as np
import pandas as pd
import matplotlib as mlt

df = pd.read_csv("experimento_teste_ab.csv")
df_pacientes = pd.read_csv("pacientes.csv")

'''1. Qual dos cenários tem a maior taxa de conversão'''


conversoes = df.groupby("Versão_Página").agg(total_visualizacoes=('Visitante_ID', 'count'),total_conversoes=('Conversões', 'sum')).reset_index()

# Calcular a taxa de conversão para cada cenário
conversoes['taxa_conversao'] = conversoes['total_conversoes'] / conversoes['total_visualizacoes']

# Identificar o cenário com a maior taxa de conversão
maior_taxa = conversoes.loc[conversoes['taxa_conversao'].idxmax()]

print("Taxas de Conversão por Cenário:")
print(conversoes)
print("\nO cenário com a maior taxa de conversão é:")
print(maior_taxa[["Versão_Página", 'taxa_conversao']])