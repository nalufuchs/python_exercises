from datetime import date
nasc = int(input('Insira seu ano de nascimento:  '))
ano = date.today().year
idade = ano - nasc
print(' '*20)
if idade > 18:
    print('Conforme informado, você possui {} anos. Sendo assim, você está \033[31m atrasado \033[m em {} ano(s) para seu alistamento, que ocorreu em {}.'.format(idade, (idade-18), ano-(idade-18)))
elif idade == 18:
    print('Está na hora de se alistar! \033[32m Não perca a oportunidade!\033[m')
else:
    print('Sei que está ansioso, \033[36m mas ainda faltam {} ano(s) para seu alistamento,\033[m já que sua idade atual é {} anos. \n Seu alistamento será em {}'.format((18-idade), idade, (ano+(18-idade))))