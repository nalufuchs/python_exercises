from math import factorial
c = int(input('Digite um número para verificarmos seu fatorial:   '))
#print('O resultado do seu fatorial é {}'.format(factorial(numero)))
# c = n
f = 1
print('Calculando {}! ='.format(c), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f = f * c
    c = c - 1
print(f'{f}')