class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root):
    stack = []
    result = []
    current = root
    prev = None

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack[-1]

        if current.right is None or current.right == prev:
            prev = stack.pop()
            result.append(prev.val)
            current = None
        else:
            current = current.right

    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(postorderTraversal(root))
