#Um palíndromo é uma cadeia que pode ser lida de frente para trás e de trás para
#frente. Ex: ‘SOMOS’ ‘1234321’. Implemente a função palindromo(palavra). O
#parâmetro palavra é uma string. A função deverá retornar True se for um palíndromo e
#False caso contrário.

def palindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    else: 
        return False
palavra = input("palavra: ")
print(palindromo(palavra))

