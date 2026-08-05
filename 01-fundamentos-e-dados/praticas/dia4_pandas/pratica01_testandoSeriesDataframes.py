# Aprendendo a usar DataFrames e Series pela biblioteca pandas
import pandas as pd
import xlsxwriter

notasDaSala = pd.read_csv("teste.csv", sep=';', decimal=',')
# print(notasDaSala.columns)
# nomes = notasDaSala["NOME"]
# print(nomes)
# print(notasDaSala)
# print(notasDaSala.head())
# print(notasDaSala["Resultado"].max())
# print(notasDaSala["Resultado"].min())
print(notasDaSala[["Prova 1 (valor: 4,0)", "Trabalho Valor: 2,0", "Prova 2: Valor: 2,0", "Prova 3 (trabalho: Valor: 2,0", "Resultado"]].describe())
# print(notasDaSala.dtypes)

notasDaSala.to_excel("notasDaSala.xlsx", sheet_name="Notas_CalculoII", index=False, engine='xlsxwriter')

print(notasDaSala.info())

nomeResult = notasDaSala[["NOME", "Resultado"]]
# print(nomeResult.head())
# print(nomeResult.shape)
# print(nomeResult.max())

menorNota = notasDaSala[notasDaSala["Resultado"] == notasDaSala["Resultado"].min()]
maiorNota = notasDaSala.loc[notasDaSala["Resultado"] == notasDaSala["Resultado"].max(), ["NOME", "Resultado"]]

porMatricula = notasDaSala[notasDaSala["MATRICULA"].isin(["25.2.4149"])]

prova1_on = notasDaSala[notasDaSala["Prova 1 (valor: 4,0)"].notna()]

# print(prova1_on)

# print(porMatricula[["NOME", "Resultado"]])
# print(maiorNota)
# print(menorNota[["NOME", "Resultado"]])