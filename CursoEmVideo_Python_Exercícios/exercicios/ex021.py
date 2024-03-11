nome = str(input('Digite seu nome completo:  ')).strip()
caps = nome.upper()
minuscula = nome.lower()
print('Seu nome em maiúscula é {}'.format(caps))
print('Seu nome em minúscula é {}'.format(minuscula))
print('Seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome possui {} letras'.format(nome.find(' ')))

espacos = nome.count(' ')
total = len(nome)
print(total-espacos)

dividido = nome.split()
#print (len(dividido[0]))

print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0], len(dividido[0])))

# letras = nome.replace(' ', '')
# print (letras)
# print(len(letras))



