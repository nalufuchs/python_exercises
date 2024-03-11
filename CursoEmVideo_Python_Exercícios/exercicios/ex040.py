from time import sleep
n1 = float(input('Insira a nota de sua primeira avaliação:   ').strip().replace(',', '.'))
n2 = float(input('Insira a nota de sua segunda avaliação:   ').strip().replace(',', '.'))
print('  ' * 20)
print('\033[36mO sistema está processando sua média...\033[m')
sleep(2)
media = (n1+n2)/2
if media > 7:
    print('\033[32mParabéns! \033[mVocê foi aprovado com média\033[32m {:.1f}\033[m'.format(media))
elif 5 < media < 6.9:
    print('Você está em \033[33mrecuperação!\033[m Sua nota foi \033[33m{:.1f}\033[m. \033[2mEstude mais!\033[m'.format(media))
else:
    print('Sua nota foi \033[31m{:.1f}\033[m, e, portanto, você está \033[31mreprovado!\033[m Mais dedicação na próxima vez!'.format(media))