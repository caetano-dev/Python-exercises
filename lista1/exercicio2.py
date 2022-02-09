'''
2. Crie um algoritmo que escreva os N primeiros termos de uma progressão aritmética
(PA). O primeiro termo e a razão da PA devem ser informados pelo usuário
'''

def progressao_aritmetica(repeticoes, primeiro_termo, razao):
    for i in range(repeticoes):
        print(primeiro_termo)
        primeiro_termo += razao

repeticoes = int(input("Digite a quantidade de termos: "))
primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

progressao_aritmetica(repeticoes, primeiro_termo, razao)
