#lista temporária
galera = list()
dado = list()
tmaior = tmenor = 0
for c in range (0,3):
    dado.append(str(input('Nome:  ')))
    dado.append(int(input('Idade:   ')))
    galera.append(dado[:])   #aqui eu copio as informaçoes de uma lista pra outra
    #cuidado pra nao esquecer o [:] senao no prox comando apaga td
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        tmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        tmenor += 1

print(f'Temos {tmaior} maiores e {tmenor} menores de idade')