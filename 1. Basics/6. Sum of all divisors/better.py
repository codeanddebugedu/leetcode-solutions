import math


def sumOfAllDivisors(n: int) -> int:
    Sum = 0
    for i in range(1, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                Sum += j
                if i // j != j:
                    Sum += i // j
    return Sum
