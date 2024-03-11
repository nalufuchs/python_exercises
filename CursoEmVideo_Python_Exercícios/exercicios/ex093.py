jogador =  {}
gols = []
jogador['nome'] = str(input('Nome do jogador:  ').strip().title())
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?  '))
for c in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {c}?  ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('=-' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor de {v}')
print('=-' * 20)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols!')