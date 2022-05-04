#Crie um algoritmo que leia um número N e imprima os N primeiros números
# primos. O seu programa deve fazer o MÍNIMO de interações possíveis.
number = int(input("number: "))
primo = True
for c in range(2,number):
    if number % c == 0:
        primo = False
        break
print(primo)
