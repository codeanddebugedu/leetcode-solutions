class Solution:
    def maxLen(self, n, arr):
        n = len(arr)
        prefix_sum = {}
        maxi = 0
        sum = 0
        for i in range(n):
            sum += arr[i]
            if sum == 0:
                maxi = i + 1
            else:
                if sum in prefix_sum:
                    maxi = max(maxi, i - prefix_sum[sum])
                else:
                    prefix_sum[sum] = i
        return maxi
