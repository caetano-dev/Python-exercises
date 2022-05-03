# Considere um vetor de trajetórias de 9 elementos onde cada elemento possui o valor do próximo elemento a ser lido.

vetorValor = [4,6,5,8,1,7,3,0,2]
vetorResposta = []
inicial = 0
for c in range(0, len(vetorValor)):
    proximoValor = vetorValor[inicial]
    inicial = proximoValor
    vetorResposta.append(inicial)
print(vetorResposta)

