'''
16. Crie um algoritmo que:
a) Leia e escreva o nome e a altura das moças inscritas em um concurso de
beleza, até que seja digitada o nome ‘MARIA’, que marca o final da lista, mas é
para ser computada no concurso.
b) Calcule e escreva as duas maiores alturas e quantas moças as possuem.
'''
nome = ""
alturas = []

while nome != 'MARIA':
    nome = input("Digite o nome da moça: ")
    altura = float(input("Digite a altura da moça: "))
    alturas.append(altura)
    
maiorAltura = max(alturas)
quantidadeDeMaiorAltura = alturas.count(maiorAltura)
for c in range (0, quantidadeDeMaiorAltura):
    alturas.remove(maiorAltura)

segundaMaiorAltura = max(alturas)
quantidadeDeSegundaMaiorAltura = alturas.count(segundaMaiorAltura)

print("a maior altura é " + str(maiorAltura) + " e ela aparece " + str(quantidadeDeMaiorAltura) + " vezes")
print("a segunda maior altura é " + str(segundaMaiorAltura) + " e ela aparece " + str(quantidadeDeSegundaMaiorAltura) + " vezes")
