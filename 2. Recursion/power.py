def power(b, e):
    if type(e) != int or e < 0:
        raise Exception("Invalid e value")
    if e == 0:
        return 1
    elif e == 1:
        return b
    return b * power(b, e - 1)


print(power(5, 3))
print(power(5, 1))
print(power(5, 0))
print(power(5, 2.5))
