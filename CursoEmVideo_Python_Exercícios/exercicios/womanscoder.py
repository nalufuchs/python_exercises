
'''
def dinheiro(d):
    moedas = {'Dólar Americano': 4.91,
              'Peso Argentino': 0.02,
              'Dólar Australiano': 3.18,
              'Dólar Canadense': 3.64,
              'Franco Suíço': 0.42,
              'Euro': 5.36,
              'Libra Esterlina': 6.21}
    d = d.replace(',', '.').strip()
    d = float(d)
    print(f'Pelo valor dado de R${d:.2f}:')
    for k, v in moedas.items():
        print(f'É possível adquirir o valor de {d/v:.2f} na moeda {k}.')


dinheiro('100,00')


def bonificacao(parameter:dict):
    med = sum(parameter.values()) / len(parameter)
    aprovados = []
    for v, k in parameter.items():
        if k >= med:
            aprovados.append(v)
    aprovados.sort(reverse=True)
    return print(aprovados)


funcionarios = {'Lucas': 6.7, 'Mariana': 9.5, 'Henrique': 8.3, 'Ana Luisa': 10, 'Laura': 5.7, 'Carlos': 4.9, 'Bruno': 7.0}
bonificacao(funcionarios)



lista_paises = [["Brasil", "1500"],
                ["Mexico","1519"],
                ["Inglaterra", "927"],
                ["Espanha","1978"],
                ["Escocia", "843"]]

paises_anos = []
for i, k in enumerate(lista_paises):
    temporaria = []
    temporaria.append(lista_paises[i][0])
    ano = int(lista_paises[i][1])
    temporaria.append(2023-ano)
    paises_anos.append(temporaria[:])
    temporaria.clear()
print(paises_anos)

'''

inimigos_derrotados = 0
nivel = 0

while (inimigos_derrotados < 50):
    print(f"Faltam {50 - inimigos_derrotados} inimigos para você mudar de nível!")
    inimigos_derrotados += int(input('Quantos inimigos foram derrotados até então?  '))
print("\nVocê atingiu o próximo nível!")
nivel = 1