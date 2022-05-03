# Leia um vetor de 16 posições e troque as 8 primeiras posições pelas 8 últimas posições. 
# Imprima o vetor original e o vetor trocado.

vetor = [3, 6, 14, 27, 28, 31, 42, 46, 55, 60, 71, 73, 77, 79, 81, 98]
vetorNovo = vetor[8:]
for c in range(0,8):
    vetorNovo.append(vetor[c])
print(vetorNovo)
