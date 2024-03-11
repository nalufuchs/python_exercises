aluno = {}
aluno['nome'] = str(input('Insira o nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}:  '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
print('=-' * 20)
for k, v in aluno.items():
    print(f'-- {k} é igual a {v}')

#print(f'O aluno {aluno["nome"]} possui média {aluno["média"]} e encontra-se {aluno["situação"]}')