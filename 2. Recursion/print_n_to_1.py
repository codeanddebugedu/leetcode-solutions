""" ques- print N to 1 """

""" without backtacking """


def reverse(i, n):
    if i < 1:
        return
    print(i)
    reverse(i - 1, n)


# reverse(4, 4)

""" With backtracking (also without using - )"""


def func(i, n):
    if n < i:
        return
    func(i + 1, n)
    print(i)


func(1, 4)
