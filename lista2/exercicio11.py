# Crie a função mat_maior_10(matriz). A função deve receber uma matriz genérica, de qualquer tamanho (não necessariamente quadrada) e retornar a quantidade de elementos da matriz maiores que dez.
matriz = [[3, 6, 14, 27], [28, 31, 42, 46]]
def mat_maior_10(matriz):
    count = 0
    for c in range(0, len(matriz)):
        for i in range(0, len(matriz[c])):
            if matriz[c][i] > 10:
                count+=1
    print(count)
mat_maior_10(matriz)
