"""
Time Complexity = O(log10 n), n is the number
Space Complexity = O(1)
"""


def reverseNumberOptimal(num: int) -> int:
    n = num
    reversed_number = 0
    while n > 0:
        last_digit = n % 10
        reversed_number = (reversed_number * 10) + last_digit
        n = n // 10
    return reversed_number


print(reverseNumberOptimal(1234))
