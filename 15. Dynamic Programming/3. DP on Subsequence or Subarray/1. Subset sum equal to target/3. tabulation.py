"""
Time Complexity: O(N*K)
Reason: There are two nested loops

Space Complexity: O(N*K)
"""


class Solution:

    def isSubsetSum(self, N, arr, k):
        # Initialize a 2D DP table with False values.
        n = len(arr)
        dp = [[False for j in range(k + 1)] for i in range(n)]

        # Set the first column to True since a sum of 0 is always possible with an empty subset.
        for i in range(n):
            dp[i][0] = True

        # Check if the first element of the array can be used to make the target sum.
        if arr[0] <= k:
            dp[0][arr[0]] = True

        # Fill in the DP table iteratively.
        for ind in range(1, n):
            for target in range(1, k + 1):
                notTaken = dp[ind - 1][target]  # Not taking the current element.
                taken = False
                # Check if taking the current element is possible without exceeding the target.
                if arr[ind] <= target:
                    taken = dp[ind - 1][target - arr[ind]]
                dp[ind][target] = (
                    notTaken or taken
                )  # Update the DP table with the result.

        # The final result is stored in the bottom-right cell of the DP table.
        return dp[n - 1][k]
