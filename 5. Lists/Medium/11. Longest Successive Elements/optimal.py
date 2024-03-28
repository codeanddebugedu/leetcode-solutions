from typing import *

"""
Time complexity -> O(N+2N) -> O(3N)
N is number of elements in nums

Space complexity -> O(N)
"""


from typing import *


def longestSuccessiveElements(arr: List[int]) -> int:
    my_set = set()
    # Same as my_set=set(arr)
    for num in arr:
        my_set.add(num)
    longest = 0
    for num in my_set:
        if num - 1 not in my_set:
            x = num
            count = 1
            while x + 1 in my_set:
                count += 1
                x += 1
            longest = max(longest, count)
    return longest
