'''
11. Crie um algoritimo que calcule a soma dos N primeiros números ímpares e positivos. O valor de N deve ser lido do usuário.
'''

number = int(input('Digite um número: '))
soma = 0

for i in range(1, 2*number + 1):
    if i % 2 != 0:
        print(i)
        soma = soma + i 

print("a soma é: "+str(soma))
