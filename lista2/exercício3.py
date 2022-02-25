'''
3. Leia uma frase e imprima o total de vogais, 
o total de brancos e o total do resto.
'''

frase = input(str("Digite uma frase: ")).lower()
totalDeVogais = frase.count("a") + frase.count("e") + frase.count("i") + frase.count("o") + frase.count("u")
totalDeBrancos = frase.count(" ")
totalDeCaracteres = len(frase)

print("Total de vogais: ", totalDeVogais)
print("Total de brancos: ", totalDeBrancos)
print("Resto: ", totalDeCaracteres-totalDeVogais-totalDeBrancos)