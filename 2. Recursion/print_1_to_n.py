"""
Print numbers from 1 to N
"""


# Without backtracking
def func(i, n):
    if i > n:
        return
    print(i)
    func(i + 1, n)


# With backtracking
def func2(i, n):
    if i < 1:
        return
    func2(i - 1, n)
    print(i)


if __name__ == "__main__":
    n = 5
    # func(1, n)
    func2(n, n)
