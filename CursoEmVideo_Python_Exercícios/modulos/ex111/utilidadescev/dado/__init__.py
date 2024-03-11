def leiaDinheiro(txt):
    p = 0
    while True:
        v = str(input(txt).replace(',', '.').strip())
        if v.isalpha():
            print(f'ERRO! {v} não é um preço válido')
        else:
            p = float(v)
            return p



#versão do professor
def leiadin(msg):
    válido = False
    while not válido:
        entrada = str(input(msg).replace(',','.').strip())
        if entrada.isalpha() or entrada.strip() == '':
            print('ERRO!')
        else:
            válido = True
            return float(entrada)