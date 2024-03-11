from random import randint
computador = randint(0, 10)
print('Estou pensando em um número de 0 a 10')
print('Será que você consegue adivinhar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?  '))
    palpite = palpite +1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print ('Um valor mais alto')
        elif jogador > computador:
            print('Um valor mais baixo')
print('Acertou com {} tentativas.'.format(palpite))