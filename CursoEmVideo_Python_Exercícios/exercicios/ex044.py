from time import sleep
print ('{:=^40}'.format(' LOJAS ATACADÃO '))
prod = float(input('Insira o preço do produto a ser pago. R$ ').strip().replace(',', '.').replace('.', ''))
vista = prod*0.9
cartao = prod*0.95
parcelado = prod*1.20
cores = {'lilas' : '\033[35m', 'verde' : '\033[32m', 'azul' : '\033[36m' ,  'amarelo' : '\033[33m',  'limpa' : '\033[m'}
print('Qual a forma de pagamento?')
print('\033[35m=-=\033[m'*10)
print('Lembrando que {}à vista{} existe {}10% de desconto{}'.format(cores['azul'], cores['limpa'], cores['verde'], cores['limpa']))
sleep(2)
print('no {}cartão de crédito em 1x{}  existe {}5% de desconto{},'.format(cores['lilas'], cores['limpa'], cores['verde'], cores['limpa']))
sleep(2)
print('no {}cartão de crédito{} em até 2x não entra desconto'.format(cores['lilas'], cores['limpa']))
sleep(2)
print('e a partir de 3x existe um {}juros de 20%{}'.format(cores['amarelo'], cores['limpa']))
print('\033[35m=-=\033[m'*10)
sleep(1)
print('\033[35m Digite: \033[m')
sleep(1)
pag = int(input(' [ 0 ] para valores à vista; \n [ 1 ] para 1x no cartão de crédito;\n [ 2 ] para 2x no cartão de crédito \n [ 3 ] para 3x no cartão de crédito \n  '))
if pag == 0:
    preco = vista
elif pag == 1:
    preco = cartao
elif pag == 2:
    preco = prod
elif pag == 3:
    preco = parcelado
print('Conforme selecionado, seu produto, de {} R${:.2f} {}, sairá por {} R${:.2f} {} na forma de pagamento escolhida.'.format(cores['amarelo'], prod, cores['limpa'], cores['azul'], preco, cores['limpa']))





