from datetime import date
from datetime import datetime
#datetime.now().year
dados = {}

while True:
    dados['nome'] = str(input('Insira seu nome:  ').strip().title())
    dados['nasc'] = int(input('Insira seu ano de nascimento: '))
    dados['idade'] = date.today().year - dados['nasc']
    dados['ctps'] = int(input('Insira sua carteira de trabalho: (0 se não tiver)   '))
    if dados['ctps'] == 0:
        break
    else:
        dados['contratação'] = int(input('Insira o ano de sua contração:  '))
        dados['salário'] = float(input('Insira seu salário: R$   ').strip().replace('.','').replace(',', '.'))
        dados['aposentadoria'] = dados['idade'] + (35 - (date.today().year - dados['contratação']))
        break
for i, v in dados.items():
    print(f'{i} tem o valor {v}')
