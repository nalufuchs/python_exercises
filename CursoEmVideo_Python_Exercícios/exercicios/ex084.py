nomepeso = []
galera = []
cont = 0
maior = menor = 0
while True:
    nome = str(input('Insira o nome:  '))
    nomepeso.insert(0, nome)
    peso = int(input('Insira o peso em kg:  '))
    nomepeso.insert(1, peso)
    galera.append(nomepeso[:2])
    if cont == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    cont += 1
    resp = str(input('Deseja adicionar outro cadastro? [ S / N ]  ').upper().strip().replace('kg', '')[0])
    if resp == 'N':
        break
print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi {maior} de {nomepeso[nomepeso.index(maior)-1]}')
print(f'O menor peso foi de {menor} de {nomepeso[nomepeso.index(menor)-1]}')
#Nao permite valores repetidos desse jeito se tiverem o mesmo peso