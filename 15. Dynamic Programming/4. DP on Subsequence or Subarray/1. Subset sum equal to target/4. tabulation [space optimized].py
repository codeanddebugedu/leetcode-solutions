"""
Time Complexity: O(N*K)
Reason: There are three nested loops

Space Complexity: O(K)
"""


class Solution:

    def isSubsetSum(self, n, arr, k):
        # Initialize a boolean array 'prev' with size (k + 1).
        prev = [False] * (k + 1)

        # Set the first element of 'prev' to True since an empty subset can sum up to 0.
        prev[0] = True

        # Check if the first element of 'arr' can directly contribute to the target sum 'k'.
        if arr[0] <= k:
            prev[arr[0]] = True

        # Loop through the elements of 'arr' and update 'prev' using dynamic programming.
        for ind in range(1, n):
            # Initialize a new boolean array 'cur' for the current element.
            cur = [False] * (k + 1)

            # An empty subset can always sum up to 0.
            cur[0] = True

            for target in range(1, k + 1):
                not_taken = prev[
                    target
                ]  # Previous result without including the current element.
                taken = False

                # Check if including the current element is possible without exceeding the target.
                if arr[ind] <= target:
                    taken = prev[target - arr[ind]]

                # Update 'cur' with the result for the current 'target'.
                cur[target] = not_taken or taken

            # Update 'prev' with the results for the current element 'ind'.
            prev = cur

        # The final result is stored in 'prev[k]'.
        return prev[k]
