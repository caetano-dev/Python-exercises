'''13. Crie um algoritmo para calcular a área de um triângulo qualquer, considerando que
são fornecidos os comprimentos dos seus lados. Esse programa não pode permitir a
entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.'''

hipotenusa = float(input('Digite o valor da hipotenusa: '))
cateto = float(input('Digite o valor do cateto: '))
if hipotenusa <= 0 or cateto <= 0:
    print('Não é possível calcular a área do triângulo com esses valores.')

print("A área do triângulo é: ", hipotenusa * cateto / 2)