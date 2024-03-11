dist = int(input('Qual a distância, em quilômetros, da distância que irá ser percorrida em sua viagem?  '))
preço = dist * 0.50 if dist <= 200 else dist * 0.45
print('O preço de sua viagem será R${:.2f}'.format(preço))



#if dist >= 200:
#    print('O valor a ser cobrado pela sua passagem é de R${:.2f}'.format((dist)*0.45))
#else:
#    print('O valor a ser cobrado pela sua passagem é de R${:.2f}'.format((dist)*0.50))

#if dist <= 200:
#    preço = dist *0.50
#else:
#    preço = dist * 0.45
#print('O preço de sua viagem será de R${:.2f}'.format(preço))

