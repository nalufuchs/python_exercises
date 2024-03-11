def is_even(num=0):
    is_even = False
    if num % 2 == 0 or num == 0:
        return True
    else:
        return False


print("Example:")
print(is_even(2))

# These "asserts" are used for self-checking
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True