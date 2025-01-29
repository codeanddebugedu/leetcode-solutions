"""
Time Complexity

1. Recursive Nature
The function energyUsed is recursive. In the worst case, each call to energyUsed makes 
two more recursive calls (for left and right).

2. Tree-Like Structure
This leads to a binary tree-like structure of calls, where the number of nodes 
roughly doubles at each level.

3. Height of the Tree
The maximum depth of recursion is n-1 (the index starts at n-1 and goes down to 0).

4. Total Calls
The total number of function calls is approximately 2^n - 1.

Therefore, the time complexity of the energyUsed function 
(and consequently minimumEnergy) is O(2^n).

Space Complexity

1. Recursion Stack
The main space usage comes from the recursion stack. 
The maximum depth of the stack will be n-1 in the worst case.
"""


class Solution:
    def energyUsed(self, height, index):
        if index == 0:
            return 0
        left = self.energyUsed(height, index - 1) + abs(
            height[index] - height[index - 1]
        )

        if index > 1:
            right = self.energyUsed(height, index - 2) + abs(
                height[index] - height[index - 2]
            )
        else:
            right = float("inf")
        return min(left, right)

    def minimumEnergy(self, height, n):
        return self.energyUsed(height, n - 1)
