list = []
number = int(input("number: "))
while number >= 0:
    list.append(number)
    number = int(input("number: "))

for i in range(0, len(list)-1):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            aux = list[i]
            list[i] = list[j]
            list[j] = aux
print(list)

start = 0
finish = len(list)-1
target= 50
found = False
position = 0

while found == False:
    mid = (start + finish) // 2

    if list[mid] == target:
        position = mid
        found = True

    elif list[mid] > target:
        position = mid
        finish = mid - 1

    else:
        position = mid
        start = mid + 1

    
print("The number is in the position: ", position+1)
