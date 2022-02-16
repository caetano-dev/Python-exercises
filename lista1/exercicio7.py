'''
7. Crie um algoritmo que leia 2 números inteiros positivos, A e B, e que calcule a soma
de todos os números compreendidos entre eles. Os valores A e B não devem ser
considerados no somatório. Caso A seja maior do que B deve ser enviada uma
mensagem para o usuário informando que a soma não será realizada
'''

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
soma = 0

if a > b:
    print("A soma não será realizada")
else:
    for i in range(a+1, b):
        soma += i
    print(f"A soma dos números entre {a} e {b} é {soma}")
