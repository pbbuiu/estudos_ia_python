try:
    with open("arquivo.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("O arquivo não existe")