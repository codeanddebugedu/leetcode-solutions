class Solution:
    def func(self, sum, last, nums, k, ans):
        # If the sum is zero and the number of elements is k
        if sum == 0 and len(nums) == k:
            # Add the current combination to the answer
            ans.append(list(nums))
            return
        # If the sum is less than or equal to zero or the number of elements exceeds k
        if sum <= 0 or len(nums) > k:
            return

        # Iterate from the last number to 9
        for i in range(last, 10):
            # If the current number is less than or equal to the sum
            if i <= sum:
                # Add the number to the current combination
                nums.append(i)
                # Recursive call with updated sum and next number
                self.func(sum - i, i + 1, nums, k, ans)
                # Remove the last number to backtrack
                nums.pop()
            else:
                # If the number is greater than the sum, break the loop
                break

    def combinationSum3(self, k, n):
        ans = []
        nums = []
        # Call the recursive function with initial parameters
        self.func(n, 1, nums, k, ans)
        return ans
