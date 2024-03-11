pessoa = {}
galera = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome:  '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]:  ').upper().strip()[0])
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]  ').upper().strip()[0])
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('=-' * 20)
print(f'A) Ao todo temos {len(galera)} pessoas.')
média = soma / len(galera)
print(f'B) A média de idade é {média:.1f}')
print(f'C) As mulheres cadastradas foram:', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='; ' )
print()
print('D) Lista das pessoas que estão acima da média:', end=' ')
for p in galera:
    if p['idade'] >= média:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()