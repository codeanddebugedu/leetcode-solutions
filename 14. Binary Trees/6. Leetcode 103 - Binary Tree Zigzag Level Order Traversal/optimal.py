# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        reverse = False
        queue.append(root)
        result = []
        while queue:
            level_size = len(queue)
            row = [0] * level_size
            for i in range(level_size):
                r = queue.popleft()
                index = i if not reverse else level_size - i - 1
                row[index] = r.val
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            reverse = not reverse
            result.append(row.copy())
        return result
