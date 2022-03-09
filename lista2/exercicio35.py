'''35. Jogo da subtração. Seu algoritmo deverá ler uma variável positiva T e
posteriormente mais três variáveis positivas S1, S2 e S3, sendo que estas variáveis são
obrigatoriamente menores que T. O jogo consiste de dois jogadores, J1 e J2. A cada
rodada a variável T é subtraída por uma das variáveis S1 ou S2 ou S3, escolhida pelo
jogador da rodada. Perde o jogo quando o jogador ao executar sua subtração, obtém
um valor menor do que zero. O seu programa deve apontar o jogador VENCEDOR.
'''

import random
from time import sleep

numeroT = int(input('Digite um número inteiro positivo: '))
if numeroT > 0:
    #jogador 1
    j1numeroS1, j1numeroS2, j1numeroS3 = input('Jogador 1: Digite 3 números inteiros positivos: ').split()
    escolhasJogador1 = [j1numeroS1, j1numeroS2, j1numeroS3]
    #jogador 2
    j2numeroS1, j2numeroS2, j2numeroS3 = input('Jogador 2: Digite 3 números inteiros positivos: ').split()
    escolhasJogador2 = [j2numeroS1, j2numeroS2, j2numeroS3]
else:
    print("O numero deve ser maior que 0.")
def changePlayer(jogadorDaRodada): 
    if jogadorDaRodada == "j1":
        return "j2"
    else: 
        return "j1"
jogadorDaRodada = "j1"
print("Prontos?")
sleep(3)
print("Vamos começar!")
sleep(1)
while numeroT>-1: 
    print(f"Rodada do {jogadorDaRodada}")
    sleep(1)
    if jogadorDaRodada == "j1":
        numeroEscolhido = random.choice(escolhasJogador1)
    else: 
        numeroEscolhido = random.choice(escolhasJogador2)
    print(f"O número {str(numeroEscolhido)} subtrai {str(numeroT)}!")
    sleep(1)
    numeroT = numeroT - int(numeroEscolhido)
    if numeroT < 0:
        sleep(1)
        print(f"O vencedor é {changePlayer(jogadorDaRodada)}!")
        print(f"PARABÉNS, {changePlayer(jogadorDaRodada)}!")
    else:
        jogadorDaRodada = changePlayer(jogadorDaRodada)

    









