from typing import List

"""
Time complexity = O(n) where n is the number of elements in list
We are looping two different times, so it will be O(n) + O(n).
Which equals tos O(n)

Space complexity = O(n), suppose all numbers are unique, it will take same length as list
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_dict = dict()
        for i in nums:
            my_dict[i] = 0

        j = 0
        for n in my_dict:
            nums[j] = n
            j += 1
        return j
