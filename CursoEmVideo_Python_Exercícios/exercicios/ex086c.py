matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#for de alimentação
for lin in range(0,3):   #laço de linha
    for col in range(0,3):  #laço de coluna
        matriz[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]:  '))


print('=-'*30)
#for para mostrar a matriz
for lin in range(0,3):
    for col in range(0,3):
        print(f'[{matriz[lin][col]:^5}]', end=' ')
    print()   #print vazio para que, cada vez que terminar uma sequencia de 3, quebrar a linha
