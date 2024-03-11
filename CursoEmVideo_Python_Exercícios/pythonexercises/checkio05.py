''' def longest_substr(sentence):
    if not sentence:
        return 0

    letras = {}
    maxlen = 0
    start = 0

    for contador in range(len(sentence)):
        if sentence[contador] in letras and letras[sentence[contador]] >= start:  #se a letra tá dentro da lista, o start ganha +1 e no final
            #quando reduzir no maxlen, ele reduz a soma total
            start = letras[sentence[contador]] + 1
        letras[sentence[contador]] = contador  #adiciona no dicionário subs['letra na posição end'] recebe end (0) ou seja subs['a'] = 0
        #permite que seja adicionado o contador nas letras, sendo 'c' : 2 (exemplo abcabc)
        maxlen = max(maxlen, contador - start + 1)

    return maxlen

'''''

#A MELHOR RESPOSTA
def longest_substr(s):
    start = res = 0  #start será usado para rastrear o início da substring atualmente considerada,
                     # e res (resultado) para rastrear o comprimento da substring mais longa encontrada.
    chars = {}
    for ind, char in enumerate(s):  # inicia um loop que percorre todos os caracteres da string s,
                                    # atribuindo o índice do caractere à variável ind e o caractere em si à variável char.
        if char in chars:
            start = max(start, chars[char] + 1)  #Se o caractere já estiver no dicionário chars, atualizamos a variável start
                                                # para o índice após a última ocorrência do caractere.
                                                # Isso garante que estamos rastreando
                                               #a posição de início da substring mais longa sem caracteres repetidos.
        chars[char] = ind   #Atualizamos o dicionário chars para armazenar o índice mais recente do caractere char.
                            # Isso é feito para que possamos saber quando o caractere foi visto pela última vez.

        res = max(res, ind - start + 1)  #Calculamos o comprimento da substring atualmente considerada,
                                        # que é a diferença entre o índice atual (ind) e o índice de início (start) mais 1.
                                    # Comparando esse valor com o valor anterior de res, garantimos que res sempre armazene
                                    # o comprimento da substring mais longa encontrada até o momento.

    return res


'''''
def longest_substr(s: str) -> int:
    start = []
    end = []
    maxlen = 0
    for l in s:
        if l in start:
            break
        if l not in start:
            start.append(l)
    for l in s[::-1]:
        if l in end:
            break
        if l not in end:
            end.append(l)
    if len(end) >= len(start):
        maxlen = len(end)
    elif len(start) == 0 or len(end) == 0:
        maxlen = 1
    else:
        maxlen = len(start)
    return maxlen



def longest_substr(s: str) -> int:
    count = 0
    substr = ''
    for i in s:
        if i not in substr:
            substr += i
        else:
            if count < len(substr):
                count = len(substr)
            print(substr.index(i))
            print((substr[substr.index(i)+1:]))
            print((substr.index(i)!=-1))
            substr = substr[substr.index(i)+1:]*(substr.index(i)!=-1)+i
    return max(len(substr), count)

'''


print("Example:")

print(longest_substr("ohomm"))
print(longest_substr('abcabc'))
print(longest_substr("abcdef"))
print(longest_substr("bbbbb"))
print(longest_substr("pwwkew"))
print(longest_substr("dvdf"))