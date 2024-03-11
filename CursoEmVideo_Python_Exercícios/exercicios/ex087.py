matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = colunatres = soma = 0


#for de alimentação
for lin in range(0,3):   #laço de linha
    for col in range(0,3):  #laço de coluna
        matriz[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]:  '))
        if (matriz[lin][col]) % 2 == 0:
            soma = matriz[lin][col] + soma
        if col == 2:
            colunatres = matriz[lin][2] + colunatres

#for col in range (0,3)        para ver o maior numero na linha 2 (matriz linha 1)
#    if c == 0:   primeira coluna
#        maior = matriz[1][c]
#    elif: matriz[1][c] > maior
#       maior = matriz[1][c]
#print(f'O maior valor dessa linha é {maior}')

print('=-'*30)
#for para mostrar a matriz
for lin in range(0,3):
    for col in range(0,3):
        print(f'[{matriz[lin][col]:^5}]', end=' ')
    print()   #print vazio para que, cada vez que terminar uma sequencia de 3, quebrar a linha
print('=-' * 30)
print(f'A soma dos números pares é {soma}')
print(f'A soma dos valores da terceira coluna é {colunatres}')
print(f'O maior valor na segunda linha é {max(matriz[1])}')