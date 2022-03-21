'''
30. Seu algoritmo deve ler as variáveis inteiras A e B. Posteriormente, calcule o
Máximo Divisor Comum (MDC) entre A e B e a quantidade de divisores comuns entre A
e B.
'''

variableA = int(input('Digite um número A: '))
variableB = int(input('Digite um número B: '))

dividersOfA = []
dividersOfB = []

def findDividers(variable, dividersOf):
    for i in range(1, variable+1):
        if variable % i == 0:
            dividersOf.append(i)
    return dividersOf

findDividers(variableA, dividersOfA)
findDividers(variableB, dividersOfB)

similarNumbers = []

for c in dividersOfA:
    for d in dividersOfB:
        if c == d:
            similarNumbers.append(c)

print(str(max(similarNumbers))+ " é o MMC")
print(str(len(similarNumbers))+ " é a quantidade")
