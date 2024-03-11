lanche = 'suco', 'hamburguer', 'pizza', 'pudim'
#tupla acima, nao necessariamente usa parenteses
print(lanche)
#printa toda a lista e bota parenteses
#tuplas sao imutáveis, portanto:
#lanche[1] = 'refrigerante'
#a substituição acima dá erro
'''for comida in lanche:
    print(f'Eu vou comer {comida}!')
print('Comi pra caramba!')
#ele imprime toda a lista na ordem de strings, 0, 1, 2, 3, etc
#e dá pra organizar e brincar entre colchetes, q nem str
for cont in range (0, len(lanche)):
    print(cont, end=' ')
    print(lanche[cont])'''

#existe tbm como pedir para enumerar
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')