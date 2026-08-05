import pandas as pd
import numpy as np

dados_csv = """Modelo;Acuracia;F1_Score;Tempo_Treino_Min;Status
ResNet50;0.92;0.89;120;Sucesso
BERT;0.88;0.85;180;Sucesso
RandomForest;0.74;0.71;15;Sucesso
CNN_v1;0.65;0.60;45;Erro
Llama3;0.95;0.93;300;Sucesso
XGBoost;0.82;0.79;30;Sucesso
SVM;0.58;0.52;10;Erro"""

with open("testeConhecimento.csv", "w") as f:
    f.write(dados_csv)

arq_csv = pd.read_csv("testeConhecimento.csv", sep=';')
# print(arq_csv.shape)
# print(arq_csv.head())
# print(arq_csv.columns)
# print(arq_csv.describe())

tempTreino = arq_csv["Tempo_Treino_Min"]

tempTreinoHrs = round(tempTreino / 60, 2)

# print(tempTreinoHrs)

tempTreinoHrs = pd.Series(tempTreinoHrs, name="tempoTreino")
arq_csv["Tempo_Treino_Horas"] = tempTreinoHrs
# print(arq_csv)

arq_csv["Pontuacao_Final"] = arq_csv["Acuracia"]*0.7 + arq_csv["F1_Score"]*0.3

# print(arq_csv)
modelos_top = arq_csv.loc[(arq_csv["Status"] == "Sucesso") & (arq_csv["Acuracia"] >= 0.8) & (arq_csv["Tempo_Treino_Min"] <= 200)]

print(modelos_top)
first_model = modelos_top.iloc[0, [0, -1]]

print(first_model)