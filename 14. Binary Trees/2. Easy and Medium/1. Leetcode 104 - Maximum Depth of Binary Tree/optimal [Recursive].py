"""
Time Complexity: O(N) 
where N height. 

Space Complexity: O(N) 
where N height. 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def maxDepthRecursive(root):
            if not root:
                return 0
            leftHeight = maxDepthRecursive(root.left)
            rightHeight = maxDepthRecursive(root.right)
            return 1 + max(leftHeight, rightHeight)

        return maxDepthRecursive(root)
