"""
Calculate factorial of a number
using recursion
"""


# Functional way
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# Parameterized way
def factorial1(i, sum):
    if i < 1:
        print(sum)
        return
    factorial1(i - 1, sum * i)


if __name__ == "__main__":
    print(factorial(5))
    factorial1(5, 1)
