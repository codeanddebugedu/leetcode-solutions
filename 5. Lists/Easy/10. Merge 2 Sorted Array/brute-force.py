"""
Time complexity -> O((n + m) log (n + m))
n is number of elements in a
m is number of elements in b

Space complexity -> O(n+m)
"""


def sortedArray(a: [int], b: [int]) -> [int]:
    freq = set()

    for num in a:
        freq.add(num)
    for num in b:
        freq.add(num)

    return sorted(list(freq))
