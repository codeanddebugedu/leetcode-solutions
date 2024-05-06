from typing import List


# Define the TreeNode structure
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorderTraversal(root: TreeNode) -> List[int]:
    # Initialize list to store
    # the preorder traversal result
    preorder = []

    # If the root is None, return
    # an empty traversal result
    if root is None:
        return preorder

    # Create a stack to store
    # nodes during traversal
    st = []
    # Push the root node
    # onto the stack
    st.append(root)

    # Perform iterative preorder traversal
    while st:
        # Get the current node
        # from the top of the stack
        root = st.pop()

        # Add the node's value to
        # the preorder traversal result
        preorder.append(root.val)

        # Push the right child
        # onto the stack if exists
        if root.right:
            st.append(root.right)

        # Push the left child onto
        # the stack if exists
        if root.left:
            st.append(root.left)

    # Return the preorder
    # traversal result
    return preorder


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
pre = preorderTraversal(root)
print(pre)
