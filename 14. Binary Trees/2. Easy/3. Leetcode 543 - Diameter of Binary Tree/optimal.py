# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time Complexity: O(N)
Space Complexity : O(1) as no additional data structures or 
memory is allocated.O(H)
"""


class Solution:
    diameter = 0

    def calculateHeight(self, root):
        if not root:
            return 0
        leftHeight = self.calculateHeight(root.left)
        rightHeight = self.calculateHeight(root.right)
        self.diameter = max(self.diameter, leftHeight + rightHeight)
        return 1 + max(leftHeight, rightHeight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calculateHeight(root)
        return self.diameter
