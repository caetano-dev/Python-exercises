#Crie um algoritmo que leia um número N e imprima os N primeiros números
# primos. O seu programa deve fazer o MÍNIMO de interações possíveis.
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
print(isprime(7))
