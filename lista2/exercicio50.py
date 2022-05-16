# Torres de Hanoi. Implemente a função hanoi(num), onde num é a quantidade de blocos do problema da torre de hanoi. A sua função deve dizer qual o movimento realizado e quantos blocos tem em cada torre após cada movimento.
def hanoi(numero, inicio, aux, fim):  
    if(numero == 1):  
        print('mova dico 1 de {} para {}'.format(inicio, fim))  
        return
    hanoi(numero - 1, inicio, fim, aux)  
    print('mova {} de {} para {}'.format(numero, inicio, fim))  
    hanoi(numero - 1, aux, inicio, fim)  
   
hanoi(5, 'a', 'b', 'c')
