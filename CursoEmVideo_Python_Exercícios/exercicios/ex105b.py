def notas(*n, sit=False):
    """
    -> Função para salvar notas em um dicionário.
    :param n: número de notas, podendo ser quantas necessário.
    :param sit: situação da turma, opcional.
    :return: retorna uma lista dividida em total, maior nota, menor nota e média da turma.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        if r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

resp = notas(3, 5.6, 6.8, 10, 8.9, sit=True)
print(resp)