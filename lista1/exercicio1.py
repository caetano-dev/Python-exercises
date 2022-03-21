'''
1. A prefeitura de uma cidade resolveu fazer uma pesquisa entre os seus
trabalhadores. Para isso ela coletou alguns dados como idade, sexo (M ou F) e salário.
Crie um algoritmo que leia estes dados e que escreva ao final:
a) a média salarial dos homens, a média salarial das mulheres
b) o maior salário encontrado entre as pessoas abaixo de 30 anos.
Obs: O final da leitura de dados é marcado por uma idade negativa.
'''
idade = 1
mediaSalarioHomem = 0 
homens = 0
mulheres = 0
mediaSalarioMulher = 0 
maiorSalario = 0 
salario = 0

while idade > 0:
    idade = int(input("idade: "))
    sexo = input("sexo (M ou F): ")
    salario = int(input("salário: "))

    
    if idade < 30 and idade > 0:
        if sexo == "M":
            mediaSalarioHomem += salario
            homens += 1
        elif sexo == "F":
            mediaSalarioMulher += salario
            mulheres += 1
        if salario > maiorSalario:
            maiorSalario = salario

    if idade < 0:

        if homens > 0:
            mediaSalarioHomem = mediaSalarioHomem/homens
            print("A média salarial dos homens é: ", mediaSalarioHomem)
        else:
            mediaSalarioHomem = 0

        if mulheres > 0:
            mediaSalarioMulher = mediaSalarioMulher/mulheres
            print("A média salarial das mulheres é: ", mediaSalarioMulher)
        else:
            mediaSalarioMulher = 0
            print("O maior salário acima de 30 é: ", maiorSalario)

    else:
        if sexo == "M":
            mediaSalarioHomem += salario
            homens += 1
        elif sexo == "F":
            mulheres += 1
            mediaSalarioMulher += salario