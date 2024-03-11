def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato.')


n = str(input('Qual o nome do jogador?'))
g = str(input('Número de gols:  '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':   #se tirou todos os espaços e ficou vazio
    ficha(gol=g)      #passando apenas um parametro, que é a quantidade de gol
    #assim, ao deixar apenas um parâmetro, o outro se torna aquilo q eu coloquei (desconhecido)
else:
    ficha(n,g)    #passando os 2 parametros, gol e jogador
