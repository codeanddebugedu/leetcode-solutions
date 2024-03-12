def checkPrime(num: int) -> bool:
    if num == 1:
        return False
    factors = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors += 1
    return factors == 1


print(checkPrime(1))
print(checkPrime(127))
