'''
15. Num frigorífico existem 90 bois. Cada boi traz preso em seu pescoço um cartão
contendo seu número de identificação e seu peso. Crie um algoritmo que escreva o
número e peso do boi mais gordo e do boi mais magro.
Além disso, responda: se houver dois ou mais bois com o mesmo peso, maior que
todos os demais, este algoritmo escreverá o número de qual deles?
'''
from random import randint

bois = []

for c in range(0,90):
    bois.append({"numero": c, "peso": randint(3,400)})

menorPeso = 99999
maiorPeso = 0

for c in bois:
    if int(c["peso"]) < menorPeso:
        menorPeso = int(c["peso"])

    elif int(c["peso"]) > maiorPeso:
        maiorPeso = int(c["peso"])

print("O mais pesado é " + str(maiorPeso))
print("O mais leve é " + str(menorPeso))
print("O algorítimo irá escolher o número do primeiro escolhido.")