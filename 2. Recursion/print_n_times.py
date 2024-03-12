"""
Print name N times

TC -> O(N)
SC -> O(N)
"""


def func(i: int, n: int):
    if i > n:
        return
    print("Code and Debug")
    func(i + 1, n)


if __name__ == "__main__":
    func(1, 5)
