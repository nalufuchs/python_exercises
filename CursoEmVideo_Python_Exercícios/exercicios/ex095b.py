#copia e cola do código do exercicio 93
jogador = {}
gols = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador:  ').strip().title())
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?  '))
    gols.clear()
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {c+1}?  ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]:  ').upper()[0])
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('--' * 25)
print('cod ', end=' ')
for i in jogador.keys():
    print(f'{i:<10}', end=' ')
print()
print('=-' * 25)
for k, v in enumerate(time):   #já que time é lista, precisa do enumerate, pra ver a key (k) e o valor (v)
    print(f'{k:>4} ', end=' ')
    for d in v.values():  #valor para cada dado/valor in values
        print(f'{str(d):<10}', end=' ')
    print()#informa-se que é string pq pode ser numérico
print('=-'*25)
#    print(f'O campo {k} tem o valor de {v}')   isso era do código antigo
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para sair):  '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}. Tente novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}-- ')
        for i, g in enumerate(time[busca]["gols"]):  #for indice na quantidade de gols na busca de gols
            print(f'  No jogo {i+1} fez {g} gols.') #gols é lista, usa-se enumerate, e o i+1 é só pra nao ficar jogo 0
    print('--' * 20)
print('Volte sempre!')