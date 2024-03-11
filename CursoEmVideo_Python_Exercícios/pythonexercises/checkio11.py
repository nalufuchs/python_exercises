def checkio(words: str) -> bool:
    cont = 0
    sentence = words.split()
    for word in sentence:
        if word.isalpha():
            cont += 1
            if cont >= 3:
                return True
        else:
            cont = 0
    else:
        return False


print("Example:")
print(checkio('one two 3 four five six 7 eight 9 ten eleven 12'))
