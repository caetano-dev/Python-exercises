# Leia um arquivo entrada.txt e conte quantas vezes cada letra do alfabeto (independente de ser maiúscula ou minúscula) aparece. Grave o resultado em um arquivo saida.txt, com a letra e o número de ocorrências. O arquivo saída terá o formato, por exemplo:
# A 13
# B 28
# Z 1
file = open("entrada.txt","r")
saida = open("saida.txt", "w")
linha = file.readline()
letrasUnicas = set(linha.lower())
letrasUnicas.remove(" ")
letrasUnicas.remove('\n')
print(letrasUnicas)
for c in letrasUnicas:
    linha.count(c)
    saida.write(f"{c} {linha.count(c)} \n")

file.close()
saida.close()
