from datetime import date
cont = 0
for c in range (0, 7):
    nasc = int(input('Insira seu ano de nascimento: '))
    idade = date.today().year - nasc
    if idade >= 21:
        cont = cont+1
print(f'Apenas {cont} pessoas já atingiram a maioridade, e {7 - cont} ainda não atingiram a maioridade.')





