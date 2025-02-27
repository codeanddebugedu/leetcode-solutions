"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""


class Solution:
    # Function to find the minimum element in the given BST.
    def minValue(self, root):
        while root and root.left is not None:
            root = root.left
        return root.data
