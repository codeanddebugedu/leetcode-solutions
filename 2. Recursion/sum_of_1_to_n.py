"""
Sum of numbers from 1 to N
"""


# Parameterized Way
def add(i, sum):
    if i < 1:
        print(sum)
        return
    add(i - 1, sum + i)


# Functional Way
def addition(n):
    if n == 1:
        return 1
    return n + addition(n - 1)


# add(5, 0)
x = addition(5)
print(x)
