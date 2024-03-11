n1 = float(input('Insira sua média 1:  '))
n2 = float(input('Insira sua média 2:  '))
m = (n1+n2)/2
print ('Sua média é {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média pode melhorar! Estude mais!')