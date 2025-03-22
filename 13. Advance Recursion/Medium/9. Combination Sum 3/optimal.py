class Solution:
    def func(self, n, Sum, last, nums, k, ans):
        if Sum == n and len(nums) == k:
            ans.append(list(nums))
            return
        if Sum > n or len(nums) > k:
            return

        for i in range(last, 10):
            nums.append(i)
            self.func(n, Sum + i, i + 1, nums, k, ans)
            nums.pop()

    def combinationSum3(self, k, n):
        ans = []
        nums = []
        self.func(n, 0, 1, nums, k, ans)
        return ans
