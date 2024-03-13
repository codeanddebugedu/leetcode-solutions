"""
Brute Force
TC - O(sqrt(n) + sqrt(n)*log(sqrt(n))), where n is the number
SC - O(sqrt(n)), where n is the number
"""
from math import sqrt
from typing import List


def printDivisors(n: int) -> List[int]:
    result = []
    for i in range(1, (int(n**0.5)) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)

    result.sort()
    return result

# SOLUTION - 2 (Get the divisors of a number in sorted order in optimal time)
"""
Here, 2 loops with TC O(sqrt(n)) have been used to print divisors in ascending order.
1. First Loop - 
    The loop continues as long as i * i is less than n.
    This condition ensures that we only check for divisors up to the square root of n,
    as divisors beyond the square root would already have been covered.
2. Second Loop - 
    The second loop to complete the list of divisors.
    The loop iterates from the square root of n to 1 in reverse order.
3. Example - 
    n = 36
    First Loop will run from i = 1 to i = 5, in this range divisors are 1, 2, 3, 4 

    Second Loop will run from i = 6 to i = 1. 
    for i = 6, divisor is (n/i) = 36/6 = 6
    for i = 5, (36 is not divisible by 5)
    for i = 4, divisor is (n/i) = 36/4 = 9
    for i = 3, divisor is (n/i) = 36/3 = 12
    for i = 2, divisor is (n/i) = 36/2 = 18
    for i = 1, divisor is (n/i) = 36/1 = 36

    so, final divisor list is = [1, 2, 3, 4, 6, 9, 12, 18, 36]
"""
# TC - O(sqrt(n))
# SC - O(sqrt(n))
def printDivisors_1(n: int) -> List:
    divisorLst: List = []
    i = 1
    while i * i < n:
        if n % i == 0:
            divisorLst.append(i)
        i += 1
    for i in range(int(sqrt(n)), 0, -1):
        if n % i == 0:
            divisorLst.append(n // i)
    return divisorLst
