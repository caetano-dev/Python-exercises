# Elabore um programa que calcule a quantidade de dias existentes entre duas datas. Dica: utilize as variáveis D1, M1, A1, D2, M2, A2. Por hipótese, as variáveis dos anos não precisam considerar a correção do calendário gregoriano. Lembre-se que há regras especiais de anos bissextos conforme o ano específico.

D1= int(input("digite o dia da primeira data: "))
M1= int(input("digite o mes da primeira data: "))
Y1 = int(input("digite o ano da primeira data: "))

D2= int(input("digite o dia da segunda data: "))
M2= int(input("digite o mes da segunda data: "))
Y2= int(input("digite o ano da segunda data: "))

difference_days = D2 - D1
difference_months = M2 - M1
difference_years = Y2 - Y1
print(difference_years*6*30+6*31+difference_months*30+difference_days-1)

