class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, n, arr, dep):
        arr.sort()
        dep.sort()

        ans = 1
        count = 1
        i = 1
        j = 0
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:  # one more platform needed
                count += 1
                i += 1
            else:  # one platform can be reduced
                count -= 1
                j += 1
            ans = max(ans, count)
        return ans
