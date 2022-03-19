'''
12. Crie um algoritmo que calcule a soma dos
primeiros 50 números pares. Os
primeiros números pares são: 2, 4, 6, ...
'''

sumOfNumbers = 0
number = 2
for n in range(0, 50):
    sumOfNumbers += number
    number += 2
print(f'A soma dos números pares é: {sumOfNumbers}')

