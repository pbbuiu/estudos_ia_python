import pandas as pd
import numpy as np

dados_csv = """Modelo;Acuracia;Precision;Recall;Custo_USD;RAM_GB;Status
ResNet50;0.92;0.90;0.88;12.5;8;OK
BERT_Base;0.88;0.86;0.84;45.0;16;OK
RandomForest;0.74;0.72;0.70;1.2;4;OK
CNN_Light;0.65;0.62;0.58;0.8;2;FALHA
Llama3_8B;0.95;0.94;0.92;80.0;32;OK
XGBoost;0.83;0.81;0.80;3.5;4;OK
SVM_RBF;0.58;0.55;0.50;0.5;2;FALHA
VisionTransformer;0.91;0.89;0.90;55.0;24;OK"""

#armazenando dados no csv
with open("desafio.csv", "w") as f:
    f.write(dados_csv)

#verificação de leitura de arquivo
try:
    df = pd.read_csv("desafio.csv", sep=';')
except FileNotFoundError:
    print("Arquivo nao encontrado!")
except:
    print("Houve algum erro")
else:
    print("Arquivo lido com sucesso")

try:
    with open("DataFrame.txt", "w") as f:
        # f.write(modelos_eficientes_array)
        # f.write(modelos_eficientes_df)
        # f.write(str(modelos_eficientes_array))
        f.write(str(df))
except:
    print("Erro inesperado")

limites_hardware = {"max_ram": 16, "max_custo": 50.0}

#separa as colunas do Data Frame e faz a média
numerics_numpy = df[["Acuracia", "Precision", "Recall"]].to_numpy(dtype='f')
media_metricas = np.round(numerics_numpy.mean(axis=1), 2)

#separa pelo desempenho sendo: Desempenho > 0.85 Alta performance e Desempenho < 0.85 Performance regular
desempenho = np.where(media_metricas > 0.85, "Alta performance", "Performance regular")

#adiciona o desempenho na coluna nova "Categoria" no Data Frame
desempenhoSeries = pd.Series(desempenho)
df["Categoria"] = desempenhoSeries

#adiciona a coluna "Custo_Por_RAM" dividindo o custo pela gb_Ram
df["Custo_Por_RAM"] = df["Custo_USD"] / df["RAM_GB"]

modelos_eficientes_df = df.loc[(df["Status"] == 'OK')
                            & (df["Categoria"] == "Alta performance")
                            & ((df["RAM_GB"] <= limites_hardware["max_ram"]) | (df["Custo_USD"] <= limites_hardware["max_custo"]))]
# print(modelos_eficientes.iloc[ : , [0, 1, -2, -1]])
modelos_eficientes_array = modelos_eficientes_df.to_numpy()
try:
    df.to_csv("resultados_analise.txt", sep='\t', index=False)
except:
    print("Erro inesperado")

modelos_eficientes_df.to_excel("resultados_analise.xlsx", sheet_name="results", index=False)

# print(help(modelos_eficientes_df.to_excel))
# print(type(modelos_eficientes_array))
# print(type(modelos_eficientes_df))


# help(modelos_eficientes.to_numpy)

# print(modelos_eficientes)

# print(df.head(1))

# print(type(desempenhoSeries))
# print(desempenhoSeries)

# print(desempenho.shape)
# print(desempenho.dtype)
# print(type(desempenho))
# print(desempenho)

# print(type(media_metricas))
# print(media_metricas)

# print(type(numerics_numpy))
# print(numerics_numpy)

