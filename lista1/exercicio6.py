'''
6. Crie um algoritmo que leia a quantidade e o preço de 50 produtos comprados por
uma empresa. Ao final deve ser escrito o total gasto pela empresa.
'''

quantidade = 0
preco = 0
total = 0

while quantidade < 50:
    quantidade = int(input('Digite a quantidade de produtos: '))
    preco = float(input('Digite o preço do produto: '))
    total += quantidade * preco
    quantidade += quantidade

print('O total gasto foi de R$ {:.2f}'.format(total))
