numeros = list()
maior = menor = 0

'''for c in range (0,5):
    numeros.append(int(input(f'Insira um número para a posição {c}:  ')))
#print(f'O maior número foi {max(numeros)}  localizado na posição {numeros.index(max(numeros))+1}'
#     f' e o menor número foi {min(numeros)} localizado na posição {numeros.index(min(numeros))+1}')

print(f'Você digitou os valores: {numeros}')
print(f'O maior valor digitado foi {max(numeros)} na posição {numeros.index(max(numeros))} ')
print(f'O menor valor digitado foi {min(numeros)} na posição {numeros.index(min(numeros))}')'''

#É possível verificar os valores maximos e minimos e suas posições do jeito antigo
for c in range(0, 5):
    numeros.append(int(input(f'Insira um número para a posição {c}:  ')))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(numeros):  #i de indice para saber em qual posicao esta o maior numero
    if v == maior:
        print(f'{i}...')
print(f'O menor valor digitado foi {menor} e se encontra nas posições', end=' ')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}...')
