'''
Crie um algoritmo que leia os nomes e os preços dos produtos de uma loja e que
escreva o nome do produto mais caro. Considere que o final da lista é marcado pelo
produto ‘XXX’ e que não existem preços repetidos.
'''

nome = ''
maiorPreco = 0  
preco = 0
nomeMaiorPreco = ''

while nome != 'XXX':
    nome = input('Digite o nome do produto: ')
    if nome == 'XXX':
        break
    preco = float(input('Digite o preço do produto: '))
    if preco > maiorPreco:
        maiorPreco = preco
        nomeMaiorPreco = nome

print('O produto mais caro é: {}'.format(nomeMaiorPreco))
