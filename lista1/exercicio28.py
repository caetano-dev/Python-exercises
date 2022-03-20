'''
28. Crie um algoritmo que leia um número (com qualquer número de dígitos) em uma
base numérica de ordem < 10 e calcule o número correspondente na base decimal. O
número da ordem da base (e.g., 2 para binária, 3 para ternária, 8 para octal, etc.) deve
também ser informado pelo usuário
'''

numero = int(input("Digite um número em uma base de ordem < 10: "))
numeroDaBase = int(input("Digite um número da base para ser convertido: "))

def converter (numero, numeroDaBase):
    if numero == 0:
        return '0'
    nums = []
    while numero:
        numero, r = divmod(numero, numeroDaBase)
        nums.append(str(r))
    return ''.join(reversed(nums))

print(converter(numero, numeroDaBase))
