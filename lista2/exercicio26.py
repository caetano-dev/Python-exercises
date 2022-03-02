'''26. Crie um algoritmo que leia N números
inteiros positivos e responda se é possível
formar um polígono com o mesmo'''

firstNumber = int(input('Digite o primeiro número inteiro positivo: '))
secondNumber = int(input('Digite o segundo número inteiro positivo: '))
thirdNumber = int(input('Digite o terceiro número inteiro positivo: '))

if firstNumber > 0 and secondNumber > 0 and thirdNumber > 0:
    if firstNumber + secondNumber > thirdNumber and firstNumber + thirdNumber > secondNumber and secondNumber + thirdNumber > firstNumber:
        print('É possível formar um polígono com os números informados.')
    else:
        print('Não é possível formar um polígono com os números informados.')   
