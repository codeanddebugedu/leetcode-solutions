class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, n, arr, dep):
        ans = 1
        for i in range(n):
            count = 1
            for j in range(i + 1, n):
                if (arr[i] >= arr[j] and arr[i] <= dep[j]) or (
                    arr[j] >= arr[i] and arr[j] <= dep[i]
                ):
                    count += 1
            ans = max(ans, count)
        return ans
