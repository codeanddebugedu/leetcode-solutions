from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        my_set = set()
        n = len(nums)

        # check all possible triplets
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        my_set.add(tuple(temp))

        ans = [list(item) for item in my_set]
        return ans
