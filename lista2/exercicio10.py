matriz = [[3, 6, 14, 27], [28, 31, 42, 46]]
def mat_transposta(matriz):
    matriz_invertida = [*zip(*matriz)]
    print(list(map(lambda x: list(x),matriz_invertida)))
mat_transposta(matriz)
