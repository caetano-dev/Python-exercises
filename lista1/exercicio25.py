'''
25. Crie um algoritmo que leia as taxas de juros (r) de um financiamento price (1% é
igual a 0,01), os valores das parcelas (pmt) e o número de parcelas (n). Em seguida,
calcule o valor presente do financiamento que é feito pela seguinte fórmula:
sum^n_i=1 pmt/(1+r)^i
'''

taxasDeJuros = float(input("Digite a taxa de juros: "))
valorDaParcela = float(input("Digite o valor da parcela: "))
numeroDeParcelas = int(input("Digite o numero de parcelas: "))

for c in range (0, numeroDeParcelas):
    valor = valorDaParcela / (1 + taxasDeJuros) ** c

print("Valor da parcela: %.2f" % valor)