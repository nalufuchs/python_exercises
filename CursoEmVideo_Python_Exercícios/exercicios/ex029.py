vel = int(input('Qual a sua velocidade, em km/h?  '))
if vel >= 80:
    print('Oh, não, você foi multado! O valor da sua multa será de R${:.2f}'.format((vel-80)*7))