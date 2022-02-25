'''
9. Crie uma matriz 5x5 com 1 na diagonal principal e
0 nas outras posições. Imprima a matriz no formato
tradicional de linhas e colunas.
'''

matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=' ')
    print()
