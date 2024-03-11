def max_digit(value: int) -> int:
    d = str(value)
    max = 0
    for n in d:
        n = int(n)
        if n >= max:
            max = n
            continue
    return max




print("Example:")
print(max_digit(134439))