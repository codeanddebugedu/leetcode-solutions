class Solution:
    def solve(self, nums, index, subset, result):
        if index >= len(nums):
            result.append(sum(subset))
            return
        subset.append(nums[index])
        self.solve(nums, index + 1, subset, result)
        subset.pop()
        self.solve(nums, index + 1, subset, result)

    def subsetSums(self, arr):
        result = []
        self.solve(arr, 0, [], result)
        return result
