class Solution:
    def func(self, sum, last, nums, k, ans):
        if sum == 0 and len(nums) == k:
            ans.append(list(nums))
            return
        if sum <= 0 or len(nums) > k:
            return

        for i in range(last, 10):
            if i <= sum:
                nums.append(i)
                self.func(sum - i, i + 1, nums, k, ans)
                nums.pop()
            else:
                break

    def combinationSum3(self, k, n):
        ans = []
        nums = []
        self.func(n, 1, nums, k, ans)
        return ans
