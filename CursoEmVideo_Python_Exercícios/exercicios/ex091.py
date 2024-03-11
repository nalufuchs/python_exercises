from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1' : randint(1,6), 'jogador2' : randint(1,6),
        'jogador3' : randint(1,6), 'jogador4' : randint(1,6)}
ranking = []
print('---'* 8)
for k, v in jogo.items():
    print(f'O {k} obteve: {v}')
    sleep(1)
print('=-=' * 8)
print('RANKING DOS JOGADORES')
print('=-=' * 8)
#para colocar dicionários em ordem, usa a função key=itemgetter para o sorted funcionar e acompanhada do local()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
#funcao 1 indica que tá analisando as chaves e não os valores
#sempre vai retornar como lista
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)