# Crie um vetor com 100 elementos aleatórios. Após isso faça a ordenação dos mesmos, SEM UTILIZAR O MÉTODO sort().
from random import randint
vetor = []
novoVetor = []
for i in range(0,100):
    vetor.append(randint(0,100))
for c in vetor:
    novoVetor.append(min(vetor))
    vetor.remove(min(vetor))
print(novoVetor)

