'''
5. Crie um algoritmo que imprima o peso total que será carregado por um caminhão.
Sabe-se que este caminhão carrega 25 caixas. O peso de cada caixa deve ser informado
pelo usuário.
'''

pesoDiferente = input("digite D caso as caixas tenham peso diferente.")
pesoTotal = 0

if pesoDiferente == "D":
    for i in range(25):
        peso = float(input("digite o peso: "))
        pesoTotal += float(peso)
    print(pesoTotal)
else:
    peso = float(input("digite o peso: "))
    pesoTotal = 25 * float(peso)
    print(pesoTotal)

