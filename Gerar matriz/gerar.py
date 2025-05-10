import random

# Inicializa a matriz vazia
matriz = []

# Gera a matriz com números aleatórios entre 0 e 2
for i in range(100):
    linha = [random.randint(0, 2) for _ in range(100)]
    matriz.append(linha)

# Exibe a matriz
for linha in matriz:
    print(linha)
