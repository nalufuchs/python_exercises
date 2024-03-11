pessoas= {'nome' : 'Ana', 'sexo' : 'F', 'idade' : 24}
pessoas['nome'] = 'Luana'
pessoas['peso'] = 75
for k, v in pessoas.items():
    print(f'{k} = {v}')


brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1]['Sigla'])

estado = dict()
pais = list()
for c in range (0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado:  '))
    pais.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
    for v in e.values():
        print(v)

print(estado)
print(pais)
print(e)
print(k)
print(v)
