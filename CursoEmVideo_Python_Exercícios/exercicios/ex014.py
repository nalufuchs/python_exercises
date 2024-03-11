km = float(input('Quantos quilômetros foram percorridos com o carro alugado?   '))
d = int(input('Quantos dias permaneceu alugado?  '))
p = (d*60) + (0.15*km)
print('O valor a ser pago pelo aluguel do seu carro, que viajou por {} quilômetros durante {} dias, é de R${:.2f}'.format(km,d,p))
