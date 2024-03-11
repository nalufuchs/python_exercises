campeonato = ('Botafogo', 'Palmeiras', 'Grêmio', 'Red Bull Bragantino', 'Fluminense', 'Athletico-PR', 'Flamengo', 'Fortaleza', 'Atlético-MG',
'Corinthians', 'Cuiabá', 'Cruzeiro', 'Internacional', 'São Paulo', 'Goiás', 'Bahia', 'Santos', 'Vasco', 'América-MG',  'Curitiba')
print('Os cinco primeiros no campeonato são:  {}'.format(campeonato[:5]))
print('A ordem dos times em ordem alfabética se dá por: {}'.format(sorted(campeonato)))
print('Os últimos 4 colocados no campeonato são: {}'.format(campeonato[:(len(campeonato)-5):-1]))
#print(campeonato.count('Cruzeiro'))
print('Cruzeiro encontra-se na {} posição.'.format(campeonato.index('Cruzeiro')))

#professor:
#for t in times
#ou
#print(f'Os cinco primeiros são {times[0:5]}')
#print(f'Os 4 últimos são {-4:}')
#print(f'O Cruzeiro encontra-se na posição {times.;index(''Cruzeiro'')+1}')
