
n = int(input('Quantos termos da sequência de fibonacci você gostaria de visualizar?  '))
print('~' * 50)
t1 = 0
t2 = 1
#sequencia = numero seguinte é a soma dos 2 anteriores = 0 1 1 2 3 5
contador = 3
print('{} -> {}'.format(t1, t2), end=' ')
while contador <= n:
    t3 = t1 + t2
    print('-> {} '.format(t3), end=' ')
    contador = contador+1
    t1 = t2
    t2 = t3
print(' -> FIM')
print('~' * 50)

