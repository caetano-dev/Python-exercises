matrix = []
for i in range(0,5):
    line = [] #reset the line
    line.append(int(input("number: ")))
    matrix.append(line)
sum = 0
even = 0
for i in range(0,5):
    sum += matrix[i][0]
    if matrix[i][0] % 2 ==0:
        even+=matrix[i][0]
print(matrix)
print("sum")
print(sum)
print("even")
print(even)


