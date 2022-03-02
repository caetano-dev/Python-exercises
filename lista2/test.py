'''Crie um algoritmo que leia um número decimal (com qualquer número de dígitos)
e o converta para a base hexadecimal. A resposta deve ser dada em string.'''
number = float(input("Digite um numero: "))
intenger = int(number)
hexadecimal = hex(intenger)
print(str(hexadecimal+ " é hexadecimal"))