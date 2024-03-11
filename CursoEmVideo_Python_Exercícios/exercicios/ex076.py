lista = ('Pão', 0.75, 'Leite', 6.50, 'Ovo', 12.90, 'Carne', 44.50,
         'Arroz', 5.60, 'Farinha', 4.99, 'Azeite', 7.85, 'Banana', 8.50)
print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)
n1 = 0
n2 = 1
#while n2 in range (0, len(lista)):
#    print('{:<10}  ..............................    R${:6>.2f}'.format(lista[n1], lista[n2]).strip())
#    n1 = n1 + 2
#    n2 = n2 + 2

for pos in range (0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<35}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')

