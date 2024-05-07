# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def postOrder(root):
    postorder = []

    # If the tree is empty,
    # return an empty traversal
    if root is None:
        return postorder

    # Two stacks for
    # iterative traversal
    st1, st2 = [], []

    # Push the root node
    # onto the first stack
    st1.append(root)

    # Iterative traversal to populate
    # st2 with nodes in postorder
    while st1:
        # Get the top node from st1
        root = st1.pop()

        # Push the node onto st2
        st2.append(root)

        # Push left child onto st1 if exists
        if root.left is not None:
            st1.append(root.left)

        # Push right child onto st1 if exists
        if root.right is not None:
            st1.append(root.right)

    # Populate the postorder traversal
    # list by popping st2
    while st2:
        postorder.append(st2[-1].data)
        st2.pop()

    # Return the
    # postorder traversal
    return postorder


def printList(lst):
    for num in lst:
        print(num, end=" ")
    print()


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    result = postOrder(root)

    print("Postorder traversal: ", end="")
    printList(result)
