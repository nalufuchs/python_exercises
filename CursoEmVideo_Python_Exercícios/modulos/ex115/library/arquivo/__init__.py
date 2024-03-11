from modulos.ex115.library.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
#funçao que ve se o arquivo existe


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação de um arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')
#função que cria o arquivo


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        título('PESSOAS CADASTRADAS')
        #print(a.readlines())  #readlines pega as linhas e joga numa lista
        #read lê o arquivo inteiro
        for linha in a:
            dado = linha.split(';')  #ao tirar ponto e vírgula, vira uma lista
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar (arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade} \n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Registro de {nome} adicionado.')