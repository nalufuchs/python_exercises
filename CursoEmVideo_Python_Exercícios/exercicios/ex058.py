from random import randint
tentativas = 0
print('='*20)
print(' '*10, 'VAMOS JOGAR?', ' '*10)
print('='*20)
pc = randint(0,10)
print('Estou pensando em um número de 0 a 10!')
jogador = int(input('Que número é esse?     '))
while jogador != pc:
    jogador = int(input('Você errou! Tente novamente:   '))
    tentativas = tentativas + 1
    if jogador == pc:
        print('Você ganhou! Foram necessárias {} tentativas'.format(tentativas+1))
