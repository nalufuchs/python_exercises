numero = list()
n1 = 0
menor = maior = 0
for c in range (0, 5):
    n = int(input(f'Insira o {c} número:  '))
    if c == 0:
        print(f'O número {n} foi adicionado na posição {c} na lista')
        numero.append(n)
        n = menor = maior
    if n > maior:
        print(f'O número {n} foi adicionado ao final da lista')
        numero.insert(len(numero), n)
        maior = n
    if n < menor:
        print(f'O número {n} foi adicionado antes na lista')
        numero.insert(0, n)
        menor = n
    if menor < n < maior:
        print(f'O número {n} foi adicionado ao meio da lista')
        if n > n1:
            numero.insert(2, n)
        if n < n1:
            numero.insert(1, n)
    n = n1

print(numero)
