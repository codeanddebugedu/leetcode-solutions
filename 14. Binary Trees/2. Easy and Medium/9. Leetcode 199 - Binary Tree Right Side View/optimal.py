from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reversePostOrder(self, root, level, result):
        if not root:
            return None
        if len(result) == level:
            result.append(root.val)
        if root.right:
            self.reversePostOrder(root.right, level + 1, result)
        if root.left:
            self.reversePostOrder(root.left, level + 1, result)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.reversePostOrder(root, 0, result)
        return result
