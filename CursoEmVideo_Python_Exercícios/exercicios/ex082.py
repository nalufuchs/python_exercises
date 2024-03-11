numeros = []
pares = []
impares = []
resp = 0
while True:
    n = int(input('Digite um número:  '))
    numeros.append(n)
    resp = str(input('Gostaria de continuar? [ S / N ]  ').upper().strip()[0])
    if resp in 'N':
        break
print(f'A lista completa é {numeros}')
for p in numeros:
    if p % 2 == 0:
        pares.append(p)
    else:
        impares.append(p)
print(f'Os números pares são {pares}')
print(f'Os números ímpares são {impares}')