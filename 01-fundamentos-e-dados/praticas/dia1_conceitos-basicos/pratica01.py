# para fazer comentários em python basta colocar o símbolo # antes do comentário

#podemos atribuir valores nos parâmetros para que ele seja padrão
def filtrar_com_precisao(predicoes, limite=0.80):
    return [n for n in predicoes if n >= limite]

dados_brutos = [0.55, 0.99, 1, 0.1, 0.88, 0.22, 0.77]

print("Os dados maiores que o limite eh: ", end=" ")
print(filtrar_com_precisao(dados_brutos, 0.7))
