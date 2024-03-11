def teste (b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')


def fatorial(num=1):
    f = 1
    for c in range (num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os valores fatoriais são {f1}, {f2} e {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

numero = int(input('Digite um número:  '))
print(par(numero))
if par(numero):
    print('É par!')
else:
    print('É impar!')