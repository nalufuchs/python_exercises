from time import sleep
print('\033[35m==\033[m'*16)
print('\033[35m Olá, iremos avaliar a possibilidade de empréstimo \n para realização do seu sonho de casa nova!\033[m')
print('\033[35m==\033[m' * 16)
print('Para isso, precisaremos de algumas informações:  ')
print('   '*15)
casa= float(input('Qual o valor do imóvel que gostaria de comprar?   R$ ').strip().replace('.', '').replace(',', '.'))
salario = float(input('Digite o valor de sua média salarial?  R$   ').strip().replace('.', '').replace(',', '.'))
ano = (int(input('Em quantos anos gostaria de quitar a dívida?  ').strip()))
prest = casa / ano / 12
print('\033[36mUm momento, nosso sistema está calculando...\033[m')
sleep(2)
if prest>(salario*0.3):
    print('\033[31m Sinto muito, seu empréstimo não foi aprovado! \033[m \n Sua parcela ultrapassará 30% do seu salário, sendo de R${:.2f} mensais, \n e não será possível pagar a dívida em {} anos. '.format(prest, ano))
    print('   ' *20)
    print('\033[35mSentimos muito! \033[m')
else:
    print('\033[32m Parabéns! Seu empréstimo foi aprovado! \033[m \n Não ultrapassou 30% do seu salário, e, portanto, \n você terá uma parcela mensal de R${:.2f} por {} ano(s)'.format(prest, ano))
