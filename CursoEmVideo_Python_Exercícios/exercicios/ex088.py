from random import sample, randint
listagem = []
print('-=-' * 15)
print(f'{"JOGO DA MEGA SENA":^40}')
print('-=-' * 15)
#eu usei sample, mas o professor fez desse método que está em cinza:
#cont = 0
#quant = int(input('Quantos jogos gostaria de sortear?'  )
#tot = 1  total de jogos sorteados  (começa com 1 pq ele adiciona 1)
#jogos = []
#while tot <= quant:    sorteios a medida da resposta da pessoa
#   cont = 0
#   while True:
#       num = randint(1,60)
#       if num not in listagem:  #para evitar numeros repetidos, só adicionaria a cada diferente na lista
#           listagem.append(num)
#           cont += 1
#       if cont >= 6:
#           break
#   listagem.sort()
#   jogos.append(listagem[:])
#   tot += 1  (pra ir até o fim da listagem)
#   listagem.clear()     listagem estava acumulando, ai transfere pra uma lista final e ela vai se deletando
# for i, l in enumerate (jogos)   (para cada INDICE na LISTAGM e enumerate)
#    print(f'Jogo {i+1}: {l}')
#o i começa com 0, portanto i+1 serve para começar no 1 e o l separado é o item na lista (os 6 jogos)

while True:
    jogos = int(input('Quantos jogos você gostaria de sortear?  '))
    for c in range(0, jogos):
        numeros = sample(range(1, 60,), 6)
        numeros.sort()
        print(f'Jogo {c}: {numeros}')
        listagem.append(numeros[:])
        numeros.clear()
    break
print(f'{" Boa sorte! ":=^45}')
print(listagem)