from random import randint
from time import sleep
comp = randint(0,5)  #faz o computador pensar num numero de 0 e 15
print('-=-'*25)
print ('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-'*25)
sleep(1)
jogador = int(input('Em que número eu pensei?  ')) #jogador tenta adivinhar
print('Processando...')
sleep(2)
if jogador == comp:
    print('Parabéns! Você ganhou!')
else:
    print('Eu ganhei! Pensei no número {} e não no {}. Mais sorte na próxima vez'.format(comp, jogador))


