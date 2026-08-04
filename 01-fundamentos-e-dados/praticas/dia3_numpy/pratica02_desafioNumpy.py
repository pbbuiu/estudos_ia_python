import numpy as np

rand = np.random.default_rng(42)

notas = rand.integers(low=50, high=100, size=5*4)
notas = notas.reshape(5, 4)

mediaProvas = notas.mean(axis=1)
mediaAlunos = notas.mean(axis=0)
print("media das notas nas provas", mediaProvas)
print("media das notas dos alunos", mediaAlunos)

alunos3provas2 = notas[:2, :3]

print(notas)
print(alunos3provas2)

print("Maior que 80: ", notas[notas>80])