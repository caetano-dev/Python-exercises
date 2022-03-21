'''
. Crie um algoritmo que apure os votos de uma eleição municipal, numa cidade com
20.000 eleitores, onde concorreram quatro candidatos. Um servidor da Justiça
Eleitoral digitará cada voto individualmente. Cada voto equivale a um número inteiro.
Os votos válidos podem ser 1, 2, 3 e 4, e estão relacionados aos seguintes candidatos:
1  João da Silva
2  José Ramalho
3  Maria Mattos
4  Pedro Américo
Votos com o valor 0 devem ser contabilizados como votos em branco, e votos com
qualquer outro valor (além de 0, 1, 2, 3 e 4), devem se considerados votos nulos.
Calcule e escreva o total de votos de cada candidato, o total de votos brancos e o total
de votos nulos.
'''
from random import randint

joaoDaSilva = 0
joseRamalho = 0
mariaMattos = 0
pedroAmerico = 0
branco = 0
nulo = 0

for c in range (0, 20000):
    voto = randint(0, 5)
    if voto == 0:
        branco += 1

    elif voto == 1:
        joaoDaSilva += 1

    elif voto == 2:
        joseRamalho += 1

    elif voto == 3:
        mariaMattos += 1

    elif voto == 4:
        pedroAmerico += 1

    else:
        nulo += 1
    
print("João da Silva: ", joaoDaSilva)
print("Jose Ramalho: ", joseRamalho)
print("Maria Mattos: ", mariaMattos)
print("branco: ", branco)
print("nulo: ", nulo)
