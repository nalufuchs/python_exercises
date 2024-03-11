def sum_numbers(text: str) -> int:
    dividido = text.split()
    num = 0
    for palavras in dividido:
        if palavras.isnumeric():
            n = int(palavras)
            num = num + n
        else:
            continue
    return num




#print("Example:")
#print(sum_numbers("hi"))

# These "asserts" are used for self-checking
#print(sum_numbers("hi"))
print(sum_numbers("This picture is by Anna Petersen between 1845 and 1910 year"))
print(sum_numbers("my numbers is 2"))