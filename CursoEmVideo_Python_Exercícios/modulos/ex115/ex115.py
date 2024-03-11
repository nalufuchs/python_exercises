def cadastrar():
    pessoa = {}
    n = pessoa['nome'] = input('Insira o nome a ser cadastrado: ')
    i = pessoa['idade'] = int(input('Insira a idade: '))
    print(f'Registro de {pessoa['nome']} cadastrado')
    cadastro.append(pessoa.copy())
    pessoa.clear()

cadastro = [{'nome': 'Pedro Paulo Pereira', 'idade': 34},
            {'nome': 'Joaquina Da Silva', 'idade': 29},
            {'nome': 'Marcio Lucas Machado', 'idade': 45},
            {'nome': 'Felipe Andrones', 'idade': 32},
            {'nome': 'Maria Luiza Silva Conceição', 'idade': 65},
            {'nome': 'Ana Claudia Carlota Silva', 'idade': 22}]

def título(txt):
    print('-' * 40)
    print(f'{txt:^40}')
    print('-' * 40)


'''
while True:
    título('MENU PRINCIPAL')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-' * 40)
    o = int(input('Sua opção:  '))
    print('-' * 40)
    if o == 3:
        título('SAINDO DO SISTEMA...')
        print('Até logo!')
        break
    if o == 1:
        título('PESSOAS CADASTRADAS')
        for k in cadastro:
            print(f'{k["nome"]:<30}', end='')
            print(f'{k["idade"]:>5} anos')
    if o == 2:
        título('NOVO CADASTRO')
        pessoa = {}
        pessoa['nome'] = input('Insira o nome a ser cadastrado: ')
        pessoa['idade'] = int(input('Insira a idade: '))
        print(f'Registro de {pessoa['nome']} cadastrado')
        cadastro.append(pessoa.copy())
        pessoa.clear()
'''


print(cadastrar())