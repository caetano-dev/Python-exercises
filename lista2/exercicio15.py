# Escreva uma função para condensar os elementos de uma lista ordenada L, que contém inteiros repetidos. Por exemplo, para L = [3, 3, 3, 3, 7, 7, 13, 13, 23], a função retorna ['3^4', '7^2', '13^2', '23'] (repare que são strings). Note-se que no caso de um número aparecer uma única vez, não deve haver expoente unitário.
l = [3, 3, 3, 3, 7, 7, 13, 13, 23]
condensed = []
uniqueElements = set(l)
for n in uniqueElements:
    if l.count(n)!= 1:
        condensed.append(str(n)+"^"+str(l.count(n)))
    else:
        condensed.append(str(n))
print(condensed)

