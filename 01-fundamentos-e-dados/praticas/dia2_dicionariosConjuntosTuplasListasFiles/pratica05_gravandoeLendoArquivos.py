f = open("arquivosTeste.txt", "w")
f.write("Esse é o meu primeiro arquivo.\n")
f.write("Estou aprendendo tecnicas para manipular")
f.write(" e também conseguir extrair textos em arquivos")

f.close

f = open("arquivosTeste.txt")
print(f.read())