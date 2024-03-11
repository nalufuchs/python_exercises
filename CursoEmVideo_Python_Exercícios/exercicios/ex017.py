import math
c1 = float(input('Digite o valor do cateto oposto:   '))
c2 =float(input('Digite o valor do cateto adjacente:   '))
h2 = math.hypot(c1, c2)
#h2 = (c1**2 + c2**2)**(1/2)
print('Em um triângulo retângulo de catetos {}, {}, o valor da hipotenusa é {:.3f}'.format(c1,c2, h2))
