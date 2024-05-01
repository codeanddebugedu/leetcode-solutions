def sumOfAllDivisors(n: int) -> int:
    Sum = 0
    for i in range(1, n + 1):
        Sum += i * (n // i)
    return Sum
