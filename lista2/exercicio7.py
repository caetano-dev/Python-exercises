# Um anagrama (do grego ana = "voltar" ou "repetir" + graphein = "escrever") é uma espécie de jogo de palavras, resultando do rearranjo das letras de uma palavra ou frase para produzir outras palavras, utilizando todas as letras originais exatamente uma vez. Um exemplo conhecido é o nome da personagem Iracema, claro anagrama de América, no romance de José de Alencar. Implemente a função anagrama(frase1,frase2). Os parâmetros frase1 e frase2 são string. A função deverá retornar True se
# forem anagramas e False caso contrário. Despreze acentuação (por exemplo: ã = a e ç = c) e os espaços não devem ser computados para efeitos do anagrama.


palavra1 = input("palavra 1: ")
palavra2 = input("palavra 2: ")

def anagrama(palavra1,palavra2):
    for c in palavra1:
        if c in palavra2:
            return True
        else:
            print("não é anagrama")
            break
if anagrama(palavra1, palavra2) == True:
    print("é anagrama")


