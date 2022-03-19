'''22. Crie um algoritmo que leia um número N e calcule:
n
∑ 1/i
𝑖=1
'''

number = int(input("Digite um número: "))
sum = 0

for n in range (1, number+1):
    sum += 1/n
    
print("A soma é: ", sum)
