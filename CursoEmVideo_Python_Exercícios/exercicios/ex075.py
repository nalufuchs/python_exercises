num = ( int(input('Digite um número:  ')),
        int(input('Digite outro número:  ')),
        int(input('Digite mais um número:  ')),
        int(input('Digite o último número:  ')))
print(f'Você digitou os valores {num}')
print('O valor 9 apareceu {} vezes'.format(num.count(9)))
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
    print('O valor 3 não apareceu em nenhuma posição')
print('Os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

numero = []
for n in range (1, 5):
    input = int(input('Digite um numero'))
    numero.append(input)




