lista = []
for c in range (0, 4):
    n = int(input('Digite um valor:  '))
    if c == 0 or n > lista[-1]:   #serve lista[len(lista)-1]
        lista.append(n)
        print(c)
#    elif n > lista[len(lista)-1]:   #serve lista[-1]
        print(f'O número {n} foi adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(pos)
                print(n)
                print(lista[pos])
                print(lista)
                print(f'O número {n} foi adicionado ao na posição {pos} da lista')
                break
            pos = pos + 1
            print(pos)
print(len(lista))
print(lista[len(lista)-1])
print(lista[-1])
print(lista)