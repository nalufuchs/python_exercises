from random import randint

print('''Vamos jogar jo ken pô? Suas opções são:'
      [ 0 ] = PEDRA
      [ 1 ] = PAPEL
      [ 2 ] = TESOURA''')
jogador = int(input('Escolha uma das opções:  '))
jokenpo = ('Pedra', 'Papel', 'Tesoura')
#pc = jokenpo[randint(0, 2)]
comp = randint(0,2)
print('=-'*12)
print('O computador escolheu {}'.format(jokenpo[comp]))
print('Você escolheu {}'.format(jokenpo[jogador]))
print('=-'*12)
print (' JÔ \n KEN \n PÔ!')

if comp == jogador:
            print('EMPATE! Você e a máquina escolheram {}'.format(jokenpo[comp]))
elif comp == 0: #pc jogou pedra
    if jogador == 1:
        print('Você ganhou! Pois jogou PAPEL e a máquina jogou PEDRA!')
    elif jogador == 2:
        print('Você perdeu! Pois tesoura perde para pedra!')
elif comp == 1: #pc jogou papel
    if jogador == 0:
        print('Você perdeu! Pois papel ganha de pedra!')
    elif jogador == 2:
        print('Você ganhou, pois tesoura ganha de papel!')
elif comp == 2: #pc escolheu tesoura
    if jogador == 0:
        print('Você ganhou! Pedra ganha de tesoura!')
    elif jogador == 1:
        print('Você perdeu! Papel perde para tesoura!')

