s = 0
for n in range (1, 7):
    n = int(input('Digite um número:  '))
    if n % 2 == 0:
        s = n + s
print(f'A soma de seus números pares digitados resultou: {s}')