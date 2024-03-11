import colorama


colorama.init()

nome_usuario = 'Ana'

def imprimir_no_log(texto, nivel='info'):
    if nivel == 'info':
        print(f'[INFO] {texto}')
    elif nivel == 'alerta':
        print(f'[ALERTA] {texto}')
    elif nivel == 'erro':
        print(f'[ERRO] {texto}')
    else:
        print(f'[ERRO] NIVEL "{texto}" não é válido')

#Aula de bibliotecas cores
def cor_colorama(color, txt):
    if color == 'yellow':
        print(colorama.Fore.YELLOW + txt)
        print(colorama.Style.RESET_ALL + txt)
    elif color == 'blue':
        print(colorama.Fore.LIGHTBLUE_EX + txt)
        print(colorama.Style.RESET_ALL + txt)
    elif color == 'red':
        print(colorama.Fore.RED + txt)
        print(colorama.Style.RESET_ALL + txt)
    else: 
        print(colorama.Fore.RED + 'ERRO' + colorama.Style.RESET_ALL)


cor_colorama('blue', 'Ana Banana')
