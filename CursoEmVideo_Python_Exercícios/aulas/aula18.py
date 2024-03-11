nome = list()
nome.append('Maria')
nome.append('20')
print(nome)
galera = list()
#galera.append(nome)  #aqui foi adicionado = portanto elas se correlacionam, então uma alteração  muda a outra
galera.append(nome[:])
nome[0] = ('João')
nome[1] = 40
galera.append(nome)
print(galera)
print(galera[0]) #print da categoria 0
print(galera[0][0]) #print da categoria 0 e da palavra 0 na lista

for p in galera:
    print(p) #mostra nome e idade
    print(p[0])  #mostra só o nome
    print(f'{p[0]} tem {p[1]} anos de idade')