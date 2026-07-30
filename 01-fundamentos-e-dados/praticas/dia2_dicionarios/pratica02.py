metricas = {"acuracia": 0.95, "precisao": 0.89, "recall": 0.92}

for chave, valor in metricas.items():
    print(f"Metricas: {chave:8s} -> Valor: {valor:.2f}")

config = {"lr": 0.001, "batch_size": 32}

epocas = config.get("lr", "Erro não existe")
print(epocas)

metricas = ['"acuracia": 0.95', '"precisao": 0.89', '"recall": 0.92']
if '"acuracia": 0.95' in metricas:
    print("Fato venerico\n")