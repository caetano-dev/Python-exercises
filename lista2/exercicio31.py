'''
31. Implemente seguinte algoritmo de criptografia: dada uma frase qualquer, se o
código ASCII do caractere for par, subtraia três do código ASCII. Se for ímpar, some três
(semelhante ao exemplo dado em sala).
'''

frase = input("Escreva uma frase: ")
for i in frase:
    if ord(i) % 2 == 0:
        print(chr(ord(i) - 3), end="")
    else:
        print(chr(ord(i)), end="")
