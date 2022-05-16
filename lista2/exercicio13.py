# Crie a função multiplica_matriz(mat1, mat2) que deve retornar o produto de duas matrizes bidimensionais genéricas, sem alterar as matrizes originais. A função deve imprimir uma mensagem de erro e retornar um vetor vazio ([]) caso não for possível realizar o produto das duas matrizes.
matriz1 = [[3, 6, 14, 27], [4, 2, 11, 69]]
matriz2 = [[3, 6, 14, 27], [28, 31, 42, 46]]
resultado = [[0, 0, 0, 0], [0, 0, 0, 0]]

def multiplica_matriz(mat1,mat2):
    try:
        for i in range(len(mat1)):
            for c in range(len(mat2[0])):
                for k in range(len(mat2)):
                    resultado[i][c] += mat1[i][k] * mat2[k][c]
        for r in resultado:
            print(r)
    except (IndexError):
            print("matrizes não são válidas")
multiplica_matriz(matriz1,matriz2)

