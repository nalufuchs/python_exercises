jogador = {}
time = []   #[{jogador 1}, { jogador 2} etc]
gols = []
total = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: ').title().strip())
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?  '))
    for c in range (0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {c}?  ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    resp = str(input('Quer continuar? [S/N]:  '))
    if resp in 'Nn':
        break
print('=-'*20)
print(f'{"cod":<5} {"nome":<7} {"gols":<7} {"total":<3}')
for i, v in enumerate(time):
    print(f'{i:<5}{time[i]["nome"]:<7} {time[i]["gols"]}        {time[i]["total"]:<3}')
print('--' * 20)
while True:
    lev = int(input('Gostaria de mostrar dados de qual jogador? 999 para sair. '))
    if lev == 999:
        break
    else:
        print('--'*20)
        print(f'LEVANTAMENTO DOS DADOS DO JOGADOR {time[lev]["nome"]} ')
#        for j, k in enumerate(time):
#            for gols in k:
#                print(f'No jogo {j} fez {gols} gols.')