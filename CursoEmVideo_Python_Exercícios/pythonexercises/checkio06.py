'''''
def longest_substr(s: str) -> int:
    txt = s
    palavra = ""
    maior_palavra = ""

    for letra in txt:
        if letra in palavra:
            palavra = letra
            continue

        if len(palavra) >= len(maior_palavra):
            maior_palavra = palavra + letra
            palavra = maior_palavra
        else:
            palavra += letra
    return 
'''''

def count_occurrences(main_str: str, sub_str: str) -> int:
    count = 0
    index = 0

    # Converter ambas as strings para minúsculas para não diferenciar maiúsculas de minúsculas
    ms = main_str.lower()
    sub = sub_str.lower()

    while True:
    # Encontrar a próxima ocorrência da substring a partir do índice atual
        index = ms.find(sub, index)
    # Se não houver mais ocorrências, sair do loop
        if index == -1:
            break
    # Incrementar a contagem e avançar o índice para evitar a mesma ocorrência
        count += 1
        index += 1


print(count_occurrences('appleappleapple', 'appleapple'))
print(count_occurrences("HELLO WORLD", "WORLD"))
print(count_occurrences("hello world hello", "o w"))
print(count_occurrences("apple apple apple", "apple"))