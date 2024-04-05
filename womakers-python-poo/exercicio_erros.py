def calcular_media(valores):
    tamanho = 1
    soma = 0.0

    for i, valor in enumerate(valores):
        soma += valor
        i +=1
        tamanho = i  #Tamanho estava no escopo fora do loop, então o valor do comprimento da lista não era considerado na médiaf
    media = soma / tamanho
    return media  #A função não possuía retorno


continuar = True
valores = []

while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:  ')
    if valor.isnumeric(): #Evita que letras e qualquer coisa não numérica seja adc na lista
        valor = int(valor)  #Como será cálculo, deverá ser necessário a averiguação que não é str e int que estará sendo realizado 
        valores.append(valor) 
    elif valor.lower() == 'ok' or 'ok' in valor.lower(): #Elif ao invés de if, pq se for número, não será OK e detectando diferentes tipos de "ok"a
        continuar = False #false é com F maiúsculo


media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))