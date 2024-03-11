def metade(preço=0, formato=False, resumo=True):
    res = preço/2
    return res if formato is False else moeda(res)
#default é resultado normal, se não, formatado no moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if not formato else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)

def moeda(preço=0, moeda='R$'):  #moeda parâmetro dentro da moeda função
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxamais=0, taxamenos=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado:"} \t{moeda(preço)}')
    print(f'{"Dobro do preço:"} \t{dobro(preço,True)}')
    print(f'{"Metade do preço:"} \t{metade(preço, True)}')
    print(f'{taxamais}{"% de aumento:"} \t{aumentar(preço, taxamais, True)}')
    print(f'{taxamenos}{"% de redução:"} \t{diminuir(preço, taxamenos,True)}')
    print('-' * 30)