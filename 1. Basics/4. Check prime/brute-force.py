"""
TC -> O(n) where n is the number
SC -> O(1)
"""


def checkPrime(num: int) -> int:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(checkPrime(2))
print(checkPrime(3))
print(checkPrime(10))
