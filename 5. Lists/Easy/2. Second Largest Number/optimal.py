"""
We are using 1 loop only, so TC will be O(N).

Time complexity = O(N) where N is the number of elements in list
Space complexity = O(1)
"""

# In previous solution we tried to do by 2 FOR loops.
# Can we solve this using single for loop? (Single pass solution?)

from typing import List


def getSecondOrderElements(n: int, a: List[int]) -> List[int]:
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")

    for i in range(0, len(a)):
        if a[i] < small:
            second_small = small
            small = a[i]
        elif a[i] < second_small and a[i] != small:
            second_small = a[i]
        if a[i] > large:
            second_large = large
            large = a[i]
        elif a[i] > second_large and a[i] != large:
            second_large = a[i]

    return [second_large, second_small]
