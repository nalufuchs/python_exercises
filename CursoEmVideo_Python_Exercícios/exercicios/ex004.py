n = (input('Digite algo '))
print('O tipo primitivo é', type(n))
#print(n.isalnum(), n.isalpha(), n.islower(), n.isupper())
#print('{} é um número? {}'.format(n, n.isnumeric()), '{} faz parte do alfabeto? {}'.format(n, n.isalpha()))
print('{} É um número? {}'.format(n, n.isnumeric()))
print('{} é alfabetico? {}'.format(n, n.isalpha()))
print('{} está em maiúsculas? {}'.format(n, n.isupper()))
print('{} é passível de impressão? {}'.format(n, n.isprintable()))
print('É um número?', n.isnumeric())
