from modulos.ex108 import moeda

p = float(input('Insira um preço: R$  '))  #personalizando a moeda (abaixo)
print(f'A metade de R${moeda.moeda(p, 'U$')} é {moeda.moeda(moeda.metade(p))}.\n'
      f'O dobro de R${moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.\n '
      f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}.\n'
      f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}.')

#moeda.moeda porque no módulo moeda importei a função moeda
#a função moeda vai retornar sempre o R$ de algo e, se tiver outro parâmetro
#irá formatar