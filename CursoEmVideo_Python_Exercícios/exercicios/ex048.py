s = 0
contador = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
        s = s+c
print(f'A soma dos {contador} números ímpares e disíveis por três totalizados entre 1 e 500 é {s}')