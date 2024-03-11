from modulos.ex109 import moeda

p = float(input('Insira um preço: R$  '))  #personalizando a moeda (abaixo)
print(f'A metade de R${moeda.moeda(p, 'U$')} é {moeda.metade(p, True)}.\n'
      f'O dobro de R${moeda.moeda(p)} é {moeda.dobro(p, True)}.\n '
      f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}.\n'
      f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}.')

#moeda.moeda porque no módulo moeda importei a função moeda
#a função moeda vai retornar sempre o R$ de algo e, se tiver outro parâmetro
#irá formatar