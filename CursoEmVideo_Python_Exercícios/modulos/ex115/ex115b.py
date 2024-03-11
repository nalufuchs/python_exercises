from modulos.ex115.library.interface import *
from modulos.ex115.library.arquivo import *

arq = "cursoemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)



while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar uma Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        título('Ver Pessoas Cadastradas')  #opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        título('NOVO CADASTRO')
        nome = str(input('Nome:  '))
        idade = leiaInt('Idade:  ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        título('Saindo do sistema, até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')

