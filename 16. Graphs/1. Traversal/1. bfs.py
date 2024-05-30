"""
Time Complexity: O(N) + O(2E), 
Where N = Nodes, 2E is for total degrees as we traverse all adjacent nodes.

Space Complexity: O(3N) ~ O(N), 
Space for queue data structure visited array and an adjacency list
"""

from typing import List
from collections import deque


class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visited = [0] * V
        visited[0] = 1
        queue = deque([0])
        bfs = []

        while queue:
            e = queue.popleft()
            bfs.append(e)
            for node in adj[e]:
                if visited[node] == 0:
                    queue.append(node)
                    visited[node] = 1
        return bfs
