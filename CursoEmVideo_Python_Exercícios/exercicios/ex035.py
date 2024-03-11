a = int(input('Insira o valor do primeiro segmento de reta:  '))
b = int(input('Insira o valor do segundo segmento de reta:  '))
c = int(input('Insira o valor do terceiro segmento de reta:  '))
print('Verificando se é passível a existência de um triângulo com os valores informados...')
#t = (a+b)>c
if (a+b)<c or (b+c)<a or (c+a)<b:
    print('Os segmentos de retas mostrados não podem formar um triângulo')
else:
    print('Os segmentos de retas mostrados podem gerar um triângulo')
