from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1  #se for negativo, multiplica por -1 para ficar positivo
    if passo == 0:
        passo = 1
    print('=-' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
    sleep(1.5)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont = cont - passo    #serve cont -= p
        print('FIM!')


#programa principal:
contador(1,10,1)
contador(10,0,2)
print('-' * 20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início:  '))
f = int(input('Fim:  '))
p = int(input('Passo:  '))  #se o passo for negativo, ele vai somar, então entra num loop infinito
#para consertar, edita-se o passo na função
contador(i,f,p)