from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: If the height list is empty or has less than 3 elements, no water can be trapped.
        if not height or len(height) < 3:
            return 0

        # Initialize two pointers and variables to keep track of maximum heights.
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        trapped_water = 0

        # Traverse the elevation map using two pointers.
        while left < right:
            # Compare the heights at both pointers.
            if height[left] < height[right]:
                # Calculate water trapped at the left index.
                if height[left] >= leftMax:
                    leftMax = height[left]  # Update leftMax.
                else:
                    trapped_water += leftMax - height[left]  # Water trapped.
                left += 1  # Move left pointer to the right.
            else:
                # Calculate water trapped at the right index.
                if height[right] >= rightMax:
                    rightMax = height[right]  # Update rightMax.
                else:
                    trapped_water += rightMax - height[right]  # Water trapped.
                right -= 1  # Move right pointer to the left.

        return trapped_water
