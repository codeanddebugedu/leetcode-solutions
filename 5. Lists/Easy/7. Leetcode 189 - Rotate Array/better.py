from typing import List

"""
Time Complexity = O(n)

Space Complexity = O(n)
This space complexity arises because you are creating a new list
of size n-k (nums[n-k:]) and another list of size k (nums[:n-k]) 
during the rotation operation. 
Although the rotation is performed in place, slicing operations 
create new lists, which consume additional memory proportional to the 
size of the original list. Therefore, the overall space complexity is O(n).
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        # Rotate the list inplace
        nums[:] = nums[n - k :] + nums[: n - k]
