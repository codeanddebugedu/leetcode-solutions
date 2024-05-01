def sumOfAllDivisors(n: int) -> int:
    Sum = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                Sum += j
    return Sum
