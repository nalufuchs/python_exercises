def longest_word(sentence: str) -> str:
    max = 0
    cont = 0
    try:
        cut = sentence.split()
        for c in range(0, len(cut)):
            if c == 0:
                max = len(cut[0])
                cont = 0
            elif len(cut[c]) > max:
                max = len(cut[c])
                cont = c
        return cut[cont]
    except IndexError:
        return sentence


print(longest_word("This is the longest sentence"))
print(longest_word(" "))


#RESPOSTA MAIS CLEAN
''''
def longest_word(sentence: str) -> str:
    strings = sentence.split()
    length = 0
    word = ""
    for s in strings:
        if len(s) > length:
            length = len(s)
            word = s
    return word
    
    
    #RESPOSTA MAIS CRIATIVA
def longest_word(sentence: str) -> str:
    sentence_sorted = sorted(sentence.split(' '), key=len, reverse=True)
    return sentence_sorted[0]

#mais RÁPIDA
def longest_word(sentence: str) -> str:
    # your code here
    return max(sentence.split(" "),key=len)


'''