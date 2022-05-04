 # Seu algoritmo deve ler as variáveis inteiras A e B. Posteriormente, calcule o Máximo Divisor Comum (MDC) entre A e B, a quantidade de divisores comuns entre A e B e o Mínimo Múltiplo Comum (MMC) entre A e B

mdc = 0
mmc = 0
divisores=0

multiplosA=[]
multiplosB=[]

numeroA = int(input("digite a "))
numeroB = int(input("digite b "))

for c in range(1, numeroB+1):
    if numeroA % c == 0 and numeroB % c ==0:
        divisores+=1
        mdc=c

for c in range(1, numeroB+1):
    multiplosA.append(c*numeroA)
    multiplosB.append(c*numeroB)

for i in range(0, len(multiplosB)):
    if multiplosA[i] in multiplosB:
        mmc = multiplosA[i]

print("divisores:"+ str(divisores))
print("mdc:"+ str(mdc))
print("mmc:"+ str(mmc))
