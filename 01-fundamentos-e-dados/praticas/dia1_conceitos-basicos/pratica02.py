#criação de uma acuracia de IA

def acuraciaIA(nome, acuracias):
    return [f"{name}: {acur}" for name, acur in zip(nome, acuracias) if acur > 0.5]

modelos = ['Modelo A', 'Modelo B', 'Modelo C', 'Modelo D']
acurs = [0.25, 0.55, 0.64, 0.86]

teste_zip = acuraciaIA(modelos, acurs)

print(teste_zip)