
#matriz = [[], [], [], [], [], [], [], [], []]
pos = 0
#for valor in matriz:
#    num = int(input('Insira um número:  '))
#    matriz[pos].append(num)
#    pos = pos + 1
#print(matriz)

matriz = []
linha = [[], [], []]
coluna = [[], [], []]

while True:
    for c in range(0,3):
        n = int(input('Insira um número:  '))
        linha[pos].append(n)
    pos += 1
    if pos == 3:
        break
pos = 0
while True:
    for col in range (0,3):
        coluna[pos].append(linha[col][pos])
    pos += 1
    if pos == 3:
        break

matriz.append(linha[:])
matriz.append(coluna[:])
#print(linha)
#print(coluna)
#print(matriz)
print(matriz[0][0])
print(matriz[0][1])
print(matriz[0][2])
print(linha)
print(coluna)
