'''
17. Uma certa firma fez uma pesquisa para saber se as pessoas gostaram ou não de um
novo produto lançado no mercado. Para isso, forneceu o sexo do entrevistado e sua
resposta (sim ou não). Sabendo-se que foram entrevistadas 2.000 pessoas, crie um
algoritmo que calcule e escreva:

a) o número de pessoas que responderam sim;
b) o número de pessoas que responderam não;a porcentagem de pessoas do
sexo masculino que responderam não.
'''
from random import randint 

sim = 0
nao = 0
man = 0

for c in range (0, 2000):
    answer = randint(0,1)
    sex = randint(0,1)

    if answer == 0:
        sim += 1
    if answer == 1:
        nao += 1
        if sex == 0:
            man += 1
    
print("sim: ", sim)
print("não: ", nao)
print("porcentagem de homens que responderam não: ", float(100*man)/2000)