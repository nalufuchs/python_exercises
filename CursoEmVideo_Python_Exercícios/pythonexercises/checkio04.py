def count_vowels(text: str) -> int:
    c = 0
    t = text.strip().replace(' ', '').lower()
    for v in t:
        if v in 'aeiou':
            c += 1
    return c


print("Example:")
print(count_vowels("Hello"))


'''
#MELHOR RESPOSTA 
def count_vowels(text: str) -> int:

    return sum(char in "aeiou" for char in text.lower())


#mais criativa
def count_vowels(text: str) -> int:
    return sum(text.lower().count(i) for i in 'aeiou')
'''
