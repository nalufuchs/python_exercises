from random import sample, randint
#n = lista = sample((range(0,100)), 5)
maior = menor = 0
#professor criou uma tupla de numeros aleatorios de 1 a 10:
numeros = ( randint(1, 10), randint (1, 10), randint (1, 10), randint (1, 10), randint (1, 10))
print('Os números sorteados foram: ', end=' ')
for n in numeros:
   print(f'{n}', end = ' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print('O menor valor sorteado foi {}'.format(min(numeros)))
#print('Os números sorteados foram:', end=' ')
#for c in range (0, 5):
#    numero = randint(0, 100)
#    print(numero, end=' ')
#    if c == 1:
#        maior = numero
#        menor = numero
#    else:
#        if numero > maior:
#            maior = numero
#        if numero < menor:
#            menor = numero
#print(f'\nO maior número sorteado foi {maior} e o menor foi {menor}')



