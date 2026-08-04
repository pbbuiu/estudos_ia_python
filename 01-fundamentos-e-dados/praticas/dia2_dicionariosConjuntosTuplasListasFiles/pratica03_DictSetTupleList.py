logs_brutos = [
    ("ResNet", "gato"),
    ("YOLO", "cachorro"),
    ("ResNet", "gato"),
    ("YOLO", "carro"),
    ("ResNet", "cachorro"),
    ("YOLO", "carro")
]
dic_logs = {}
set_logs = set()
print(logs_brutos)
for modelos, tag in logs_brutos:
    set_logs.add(tag)
    if modelos in dic_logs:
        dic_logs[modelos] += 1
    else:
        dic_logs[modelos] = 1

print(dic_logs)
print(set_logs)
