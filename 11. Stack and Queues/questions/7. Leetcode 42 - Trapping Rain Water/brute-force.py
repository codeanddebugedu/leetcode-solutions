from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        n = len(height)

        # Initialize prefixMax and suffixMax arrays.
        prefixMax = [0] * n
        suffixMax = [0] * n

        # Fill the prefixMax array.
        prefixMax[0] = height[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], height[i])

        # Fill the suffixMax array.
        suffixMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], height[i])

        # Calculate the total water trapped.
        trapped_water = 0
        for i in range(n):
            # Water trapped at the current index.
            trapped_water += min(prefixMax[i], suffixMax[i]) - height[i]

        return trapped_water
