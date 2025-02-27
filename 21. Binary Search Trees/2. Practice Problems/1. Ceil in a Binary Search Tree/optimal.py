class Solution:
    def findCeil(self, root, inp):
        ceil = -1
        while root is not None:
            if root.key == inp:
                return root.key
            elif inp < root.key:
                ceil = root.key
                root = root.left
            else:
                root = root.right
        return ceil
