'''
10. Uma empresa lançou um novo produto no mercado e fez uma pesquisa para saber
se os consumidores estavam satisfeitos, para isso eles deveriam responder sim ‘S’ ou
não ‘N’. Crie um algoritmo que leia a resposta de todas as pessoas e escreva a
porcentagem dos que disseram sim e dos que disseram não.
Obs: O final da leitura de dados é marcado pela resposta ‘F’.
'''

sim = 0
nao = 0
resposta = ""
porcentagem = 0
totalDeRespostas = 0

while resposta != "F":
    resposta = input("Você gostou do nosso produto? (S ou N): ")
    
    if resposta == "S":
        totalDeRespostas += 1
        sim += 1
    elif resposta == "N":
        totalDeRespostas += 1
        nao += 1
    elif resposta == "F":
        break

print("Total de respostas: ", totalDeRespostas)
print("Porcentagem de sim: ", (sim/totalDeRespostas)*100)