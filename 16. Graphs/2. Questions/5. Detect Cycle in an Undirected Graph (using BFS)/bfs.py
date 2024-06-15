"""
Time Complexity: O(N + 2E) + O(N), 
Where N = Nodes, 2E is for total degrees as we traverse all adjacent nodes. 
In the case of connected components of a graph, it will take another O(N) time.

Space Complexity: O(N) + O(N) ~ O(N), 
Space for queue data structure and visited array.
"""

from typing import List
from collections import deque


class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [0] * V

        def bfs(start):
            queue = deque([(start, -1)])
            visited[start] = 1
            while queue:
                node, prev = queue.popleft()
                for adjNode in adj[node]:
                    if not visited[adjNode]:
                        visited[adjNode] = 1
                        queue.append((adjNode, node))
                    elif prev != adjNode:
                        return True
            return False

        for i in range(V):
            if not visited[i]:
                if bfs(i):
                    return True
        return False
