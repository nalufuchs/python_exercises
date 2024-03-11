#tpar = []
#timpar = []
#numeros = []

'''for c in range (0, 7):
    num = int(input(f'Insira o {c} valor:  '))

    if num % 2 == 0 and num != 0:
        tpar.append(num)
        tpar.sort()
    else:
        timpar.append(num)
        timpar.sort()
numeros.append(tpar[:])
numeros.append(timpar[:])
tpar.clear()
timpar.clear()
for seq in numeros:'''

numeros = [[],[]]  #duas listas, 0 e 1, na lista numero  numeros[0]
valor = 0
for c in range (1, 8):
    valor = int(input(f'Digite o {c} valor:  '))
    if valor % 2 == 0:
        #numeros.insert([0], valor) o primeiro parametro da funcao só aceita numeros inteiros, eu tinha passdo uma lista com valor 0 dentro
        numeros[0].append(valor)
    else:
        # numeros.insert(1, valor)  sem o colchete ele nao adiciona pq ele substitui literalmente pela posicao q tava, e nao coloca dentro da lista
        numeros[1].append(valor)
numeros.sort()
numeros[0].sort()
numeros[1].sort()
print(f'Todos os valores: {numeros}')
print(f'Os números pares digitados foram {numeros[0]}')
print(f'Os números ímpares digitados foram {numeros[1]}')







