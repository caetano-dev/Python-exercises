'''
9. Crie uma matriz 5x5 com 1 na diagonal principal e
0 nas outras posições. Imprima a matriz no formato
tradicional de linhas e colunas.
'''
matriz = []
for i in range(0,5):
    line = []
    for c in range(0,5):
        if i == c:
            line.append(1)
        else:
            line.append(0)
    matriz.append(line)
    print(line)
