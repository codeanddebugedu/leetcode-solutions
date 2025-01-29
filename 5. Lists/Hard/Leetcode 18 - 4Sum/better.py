from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        my_set = set()
        for i in range(0, n):
            for j in range(i + 1, n):
                hash_set = set()
                for k in range(j + 1, n):
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if fourth in hash_set:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        my_set.add(tuple(temp))
                    hash_set.add(nums[k])
        result = [list(ans) for ans in my_set]
        return result
