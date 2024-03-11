def notas(*n, sit=False):
    total = {}
    maior = menor = 0
    cont = med = 0
    for num in n:
        if cont == 0:
            maior = num
            menor = num
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        cont += 1
        med += num
    total['media'] = med/cont
    total['total'] = cont
    total['maior'] = maior
    total['menor'] = menor
    if sit:
        if total['media'] >= 7:
            total['sit'] = 'BOA'
        if 7 > total['media'] > 5:
            total['sit'] = 'RECUPERAÇÃO'
        if total['media'] <= 5:
            total['sit'] = 'REPROVADO'
    return total




resp = notas(5.5, 6.8, 10, 6.5, sit=True)
print(resp)

#{total, maior, menor, média, situacao}