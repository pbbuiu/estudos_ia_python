import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados_df = pd.DataFrame({"Alunos": ["Pablo", "Pedro", "Joao"],
                         "Notas1": [8, 9, 5], 
                         "Notas2": [10, 8, 9]}, 
                         columns=["Alunos", "Notas1", "Notas2"])
# dados_df["Media"] = np.round((dados_df["Notas1"]+dados_df["Notas2"])/2, 10)
dados_df["Media"] = (dados_df["Notas1"]+dados_df["Notas2"])/2

dados_df_renamed = dados_df.rename(index={0: "Aluno 1", 1: "Aluno 2", 2: "Aluno 3"}, columns=str.upper)

dados_ordenados = dados_df.sort_values('Notas1')
dados_ordenados.loc[1, 'Notas1'] = np.nan
dados_ordenados.loc[0, 'Alunos'] = '0'
dados_withoutNaN = dados_ordenados.loc[np.array(dados_ordenados.isna())]

transformacao_alunos = pd.to_numeric(dados_ordenados["Alunos"], errors='coerce')
print(transformacao_alunos)
print(dados_df)
# print(dados_withoutNaN)
# print(dados_ordenados)
# print(dados_ordenados.value_counts('Notas1'))
# print(dados_ordenados)

alunosComP = dados_df['Alunos'].str.contains('P')
# print(dados_df)
# print(alunosComP)
# # print(help(dados_df_renamed.rename))
# print(dados_df_renamed)
# print(dados_df)
# print(help(pd.DataFrame))