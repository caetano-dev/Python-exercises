# Um anagrama (do grego ana = "voltar" ou "repetir" + graphein = "escrever") é uma espécie de jogo de palavras, resultando do rearranjo das letras de uma palavra ou frase para produzir outras palavras, utilizando todas as letras originais exatamente uma vez. Um exemplo conhecido é o nome da personagem Iracema, claro anagrama de América, no romance de José de Alencar. Implemente a função anagrama(frase1,frase2). Os parâmetros frase1 e frase2 são string. A função deverá retornar True se
# forem anagramas e False caso contrário. Despreze acentuação (por exemplo: ã = a e ç = c) e os espaços não devem ser computados para efeitos do anagrama.

def anagrama(frase1, frase2):
    if sorted(frase1) == sorted(frase2):
        return True
    else:
        return False
print(anagrama("frase", "frase"))
    
