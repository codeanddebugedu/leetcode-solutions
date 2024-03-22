"""
Time complexity -> O(n+m)
n is number of elements in a
m is number of elements in b

Space complexity -> O(1)
"""


def sortedArray(a: [int], b: [int]) -> [int]:
    i = 0
    j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            if len(result) == 0 or result[-1] != a[i]:
                result.append(a[i])
            i += 1
        else:
            if len(result) == 0 or result[-1] != b[j]:
                result.append(b[j])
            j += 1

    while i < len(a):
        if len(result) == 0 or result[-1] != a[i]:
            result.append(a[i])
        i += 1

    while j < len(b):
        if len(result) == 0 or result[-1] != b[j]:
            result.append(b[j])
        j += 1

    return result
