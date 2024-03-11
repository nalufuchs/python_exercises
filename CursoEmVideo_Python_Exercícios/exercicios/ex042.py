from time import sleep
a = int(input('Insira o valor do primeiro segmento de reta:  '))
b = int(input('Insira o valor do segundo segmento de reta:  '))
c = int(input('Insira o valor do terceiro segmento de reta:  '))
print('  ' * 15)
print('\033[36mVerificando se é passível a existência de um triângulo com os valores informados...\033[m')
sleep (2)
print('  ' * 10)
#t = (a+b)>c
if (a+b)<c or (b+c)<a or (c+a)<b:
    print('Os segmentos de retas mostrados \033[31mnão podem formar um triângulo.\033[m')
else:
    print('Os segmentos de retas mostrados \033[32mpodem gerar um triângulo\033[m')
    print('  '*10)
    if a == b and b == c:
        print('Será um triângulo \033[36mequilátero\033[m, pois \033[2mpossui os três lados iguais\033[m.')
    elif a == b != c or a != b == c or a == c != b:
        print('Será um triângulo \033[36misósceles\033[m, pois \033[2mpossui dois lados iguais\033[m.')
    else:
        print('Será um \033[36mtriângulo\033[m escaleno, pois \033[2mtodos seus lados diferem\033[m.')
