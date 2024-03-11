numeros = [1, 2, 3, 4, 5]
print(numeros)
numeros.append(8)
print(numeros)
numeros.insert(0, 6)
print(numeros)
numeros[0] = 0
print(numeros)
numeros.remove(4)
print(numeros)

valores = list()
#valores.append(5)  #igual ao exemplo abaixo, mas os números já foram ditos, e não no input
#valores.append(4)
#valores.append(9)
#for v in valores:
#    print(f'{v}...')
#for c, v in enumerate(valores):
 #   print(f'Na posição {c}, encontrei o valor {v}')
#print('Cheguei ao final da lista')

for cont in range (0, 5):   #permite que o valor seja adicionado diversas vezes pelo range
    valores.append(int(input('Insira um valor:  ')))
for v in valores:
    print(f'{v}...')
for c, v in enumerate(valores): #ao enumerar na funcao enumerate vc consegue colocar qual posicao está na ordem colocada
    print(f'Na posição {c}, encontrei o valor {v}')
print('Cheguei ao final da lista')

a = [1, 2, 3, 4]
#b = a  aqui se igualou a lista e assim elas ficam vinculadas, toda alteração numa reflete na outra
b = a[:]   #ao selecionar assim, todos os itens são copiados, permitindo alterações numa lista sem envolver a outra
b[2] = 7
print(a)
print(b)

