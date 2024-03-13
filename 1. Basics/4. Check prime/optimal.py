"""
TC -> O(sqrt(n)) where n is the number
SC -> O(1)
"""

from math import sqrt


def checkPrime(num: int) -> int:
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


print(checkPrime(2))
print(checkPrime(3))
print(checkPrime(10))
