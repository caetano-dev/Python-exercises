number = int(input("digite um numero: "))
matrix = []

for i in range(0,number):
    matrix.append([])
    for c in range(0,number):
        if c == i:
            matrix[i].append(1)
        else:
            matrix[i].append(0)
for c in range(0,number):
    print(matrix[c])

