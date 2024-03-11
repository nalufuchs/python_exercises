sal = float(input('Qual o valor do seu salário, em R$?  ').replace(',', '.'))
if sal<=1.250:
    print('O valor de seu salário com o aumento será de R${:.2f}'.format(sal*1.15))
else:
    print('O valor do seu salário com o aumento será de R${:.2f}'.format(sal*1.10))