'''18. Crie um algoritmo que leia um número N e verifique se ele é primo.'''

numero = int(input('Digite um número: '))

if numero < 2:
    print('Não é primo.')

else:
    for i in range(2, numero):
        if numero % i == 0:
            print('Não é primo.')
            break
    else:
        print('É primo.')