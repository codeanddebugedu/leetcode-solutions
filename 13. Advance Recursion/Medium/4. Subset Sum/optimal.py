class Solution:
    def solve(self, nums, total, index, result):
        if index >= len(nums):
            result.append(total)
            return
        Sum = total + nums[index]
        self.solve(nums, Sum, index + 1, result)
        Sum = total
        self.solve(nums, Sum, index + 1, result)

    def subsetSums(self, arr):
        result = []
        self.solve(arr, 0, 0, result)
        return result
