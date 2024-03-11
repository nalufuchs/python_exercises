def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m². ')



print('CONTROLE DE TERRENOS')
print('-' * 15)

l = float(input('Largura (m):  '))
c = float(input('Comprimento(m):  '))
area(l,c)