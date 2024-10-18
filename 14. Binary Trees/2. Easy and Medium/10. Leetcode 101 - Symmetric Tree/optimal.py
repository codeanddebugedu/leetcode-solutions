from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def check(self, root1, root2):
        if (root1 and not root2) or (root2 and not root1):
            return False
        elif not root1 and not root2:
            return True
        if root1.val != root2.val:
            return False
        return self.check(root1.left, root2.right) and self.check(
            root1.right, root2.left
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)
