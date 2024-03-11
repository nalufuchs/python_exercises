temp = []   #lista temporária
princ = []   #lista principal
maior = menor = 0
while True:
    temp.append(str(input('Nome:  ')))
    temp.append(float(input('Peso:  ')))
    if len(princ) == 0:   #nada foi adicionado, nenhuma pessoa cadastrada
        maior = menor = temp[1]   #é o 1 pq o 0 é o nome e queremos o peso
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()   #para evitar acumulo de listas dentro de listas, resta o temporário
    resp = str(input('Quer continuar? [ S / N ]   '))
    if resp in 'Nn':
        break
print('=-' * 30)
#print(f'Os dados foram {princ}')
print(f'Ao todo, foram cadastrados {len(princ)} pessoas')  #ao invés de usar contador, usou-se len
print(f'O maior peso foi de {maior} Kgs e pertence a', end=' ')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]};', end=' ')
print(' ')
print(f'O menor peso foi de {menor} Kgs e pertence a', end=' ')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]};', end =' ')
print(' ')