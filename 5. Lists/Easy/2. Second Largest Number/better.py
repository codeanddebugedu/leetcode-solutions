"""
We are using 2 for loops, so it will be O(N) + O(N).
Which will be equal to O(2N)
Which then comes down to O(N)

Time complexity = O(N) where N is the number of elements in list
Space complexity = O(1)
"""

# In the previous solution, we were sorting the array, lets try to solve
# without sorting the array and thus descreasing the time complexity

from typing import List


def getSecondOrderElements(n: int, a: List[int]) -> List[int]:
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")

    # Find the smallest and largest number
    for i in range(0, len(a)):
        small = min(small, a[i])
        large = max(large, a[i])

    # Now find the second smallest and second largest
    for i in range(0, len(a)):
        if a[i] < second_small and a[i] != small:
            second_small = a[i]
        if a[i] > second_large and a[i] != large:
            second_large = a[i]
    return [second_large, second_small]
