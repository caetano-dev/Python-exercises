#Leia um arquivo entrada.txt e troque todas as letras minúsculas por maiúsculas e vice-versa. Grave o resultado em um arquivo saida.txt.
file = open("entrada.txt","r")
linha = file.readline()
novaLinha = ""
for c in linha:
    novaLinha+=c.swapcase()
file.close()
saida = open("saida.txt", "w")
saida.write(novaLinha)
saida.close()
