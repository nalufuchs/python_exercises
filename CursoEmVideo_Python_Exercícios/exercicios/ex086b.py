#86 - criar uma matriz 3x3 com valores do teclado. no final mostrar a matriz de forma correta.
matriz = [[],[],[]]

for c in range(0,3):
    for x in range(0,3):
        matriz[c].append(int(input(f'Valor [{c}][{x}]: ')))

for c in range(0,3):
    for x in range(0,3):
        print(f'[{matriz[c][x]}]', end='')
    print()