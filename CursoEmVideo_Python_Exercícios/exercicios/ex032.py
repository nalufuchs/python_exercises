from datetime import date
ano = int(input('Insira um ano e irei prever se é ou não bissexto, e, para verificar o ano atual, insira 0:  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto')
else:
    print ('O ano não é bissexto')

