soma = cont = resposta = 0
maior = menor = 0
#se eu quiser que a resposta in 'sS', posso afirmar variavel resposta = 's'
while resposta != 'S':
    n = int(input('Insira um número:  '))
    cont = cont + 1
    soma = soma + n
    #Dá pra fazer assim de maior e menor tbm:
    #if cont == 1: maior = menor = n
    #else: if num > maior: maior = n
    #if num < menor: menor = n
    menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resposta = input('Gostaria de parar? [ S / N ] ').upper().strip()[0]
media = soma / n
print(f'Os valores disponibilizados somaram {soma} e foram um total de {cont} números, sendo o maior {maior} e o menor {menor} e sua média deu {media:.2f}')