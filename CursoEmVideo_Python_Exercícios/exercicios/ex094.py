cadastro = {}
pessoal = []
nomes = []
mulheres = []
idade = mul = 0
while True:
    cadastro['nome'] = str(input('Insira o nome:  ').title())
    cadastro['sexo'] = str(input('Insira o sexo [M/F]:  ').strip().upper()[0])
    cadastro['idade'] = int(input('Insira a idade:  '))
    pessoal.append(cadastro.copy())
    idade = cadastro['idade'] + idade
    cadastro.clear()
    resp = str(input('Gostaria de continuar?[ S / N ]  ').upper().strip()[0])
    if resp in 'nN':
        break
media = idade / len(pessoal)
for c, v in enumerate(pessoal):
    if pessoal[c]['idade'] > media:
        nomes.append(pessoal[c]['nome'])
    if pessoal[c]['sexo'] in 'Ff':
        mulheres.append(pessoal[c]['nome'])

print(f'Ao final, foram cadastrados {len(pessoal)} pessoas.')
print(f'A média de idade do grupo é {media:.1f}')
print(f'As mulheres cadastradas foram {mulheres}')
print(f'As pessoas com idade acima da média foram {nomes}')
