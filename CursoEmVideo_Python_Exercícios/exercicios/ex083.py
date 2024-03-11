expressao = str(input('Digite uma expressão que contenha parênteses:  ').strip().upper().replace(' ', ''))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':  #ou a lista tá vazia, ou tá cheia
        if len(pilha) > 0:   #lista cheia
            pilha.pop() #remove o ultimo item da pilha
            #a cada adicao de um par do parenteses, ele remove, ficando "nulo"
    else:
        pilha.append(')')  #se estiver um numero a mais de parenteses fechando, tá sobrando
        break
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')


if '(' or ')' in expressao:
    a = expressao.count('(')
    b = expressao.count(')')
    print(expressao)
    print(a)
    print(b)
    if a == b:
        print('A expressão é válida')
    else:
        print('A expressão é inválida')
