'''
3. Crie um algoritmo que leia uma quantidade não determinada de números inteiros. O
programa deve calcular e escrever a quantidade de números pares e ímpares e a
média aritmética dos números pares. A leitura deve ser encerrada quando for lido o
número zero, que não deva ser considerado.
''' 
par = 0
somaPar = 0
impar = 0
numero = 1

while numero != 0:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0 and numero != 0:
        par += 1
        somaPar += numero
    elif numero % 2 != 0 and numero != 0:
        impar += 1

print("Quantidade de números pares: ", par)
print("Quantidade de números ímpares: ", impar)
print("Média dos números pares: ", somaPar/par)

