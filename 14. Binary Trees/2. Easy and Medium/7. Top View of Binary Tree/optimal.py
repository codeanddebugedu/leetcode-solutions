from collections import deque


class Solution:

    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):
        if not root:
            return None
        ans = []
        queue = deque()
        element_with_level = {}
        queue.append((root, 0))
        while queue:
            e, line = queue.popleft()
            if line not in element_with_level:
                element_with_level[line] = e.data
            if e.left:
                queue.append((e.left, line - 1))
            if e.right:
                queue.append((e.right, line + 1))
        for value in sorted(element_with_level.items()):
            ans.append(value[1])
        return ans
