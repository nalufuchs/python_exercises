n = int(input('Digite um número [999 para parar]:  '))
soma = 0
contador = 0
while n != 999:
    soma = soma + n
    contador = contador + 1
    n = int(input('Digite um número:  '))
print('Foram {} valores digitados e sua soma resultou em {}'.format(contador-1, soma))
#ao inves de adicionar -999 no soma, copiou o comando do N tanto dentro do while quanto fora
#e foi movido ao final, pois, assim, ele não vai ser somado ou considerado (pq ele ta mais pra baixo)
#assim, ao dar o valor 999, ele "salta" pra fora da line antes de ser somado ou algo assim