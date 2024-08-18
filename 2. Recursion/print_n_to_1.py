"""
Back-tracking solution to print n to 1 without minus (-) 
"""


def func(i, n):
    if i > n:
        return
    func(i + 1, n)
    print(i)


func(1, 4)
