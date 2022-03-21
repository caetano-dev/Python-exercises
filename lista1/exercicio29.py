'''
29. Crie um algoritmo que leia um número decimal (com qualquer número de dígitos)
e o converta para a base hexadecimal.
'''

numero = int(input("Digite um número em uma base de ordem < 10: "))

def converter (numero):
    if numero == 0:
        return '0'
    nums = []
    while numero:
        numero, r = divmod(numero, 16)
        nums.append(str(r))
    return ''.join(reversed(nums))

print(converter(numero))
