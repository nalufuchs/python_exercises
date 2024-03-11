def beginning_zeros(a: str) -> int:
    cont = 0
    if a[0] == '0':
        for item in a:
            if item == '0':
                cont += 1
            else:
                return cont
        return cont
    else:
        return cont




print(beginning_zeros("0000"))
print(beginning_zeros("10"))
print(beginning_zeros("100"))