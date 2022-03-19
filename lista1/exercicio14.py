'''
14. Crie um algoritmo que:
    a) Leia a idade de várias pessoas. O final da lista contém o valor da idade igual a
    -1 que deverá ser computado.

    b) Calcule e mostre a idade média desse grupo de indivíduos. Escreva também a
    porcentagem de pessoas entre 21 e 65 anos inclusive.
'''

age = 0
numberOfPeople = 0
averageAge = 0
inBetween21And65 = 0

while age != -1:
    age = int(input('Digite a idade: '))
    if age != -1:
        numberOfPeople += 1
        averageAge += age
        if age >= 21 and age <= 65:
           inBetween21And65 += 1


print("A idade média é: ", str(averageAge / numberOfPeople))
print("A porcentagem de pessoas entre 21 e 65 anos é: ", str(inBetween21And65 / numberOfPeople * 100))
