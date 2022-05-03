# Leia um vetor de 40 posições e conte quantos elementos pares se encontram no vetor.

vetor =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
contagem = 0
for c in range(0,len(vetor)):
    if vetor[c]%2==0:
        contagem+=1
print("existem "+str(contagem))
