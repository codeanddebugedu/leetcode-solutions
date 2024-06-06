from typing import List


class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [0] * V

        def dfs(node, parent):
            visited[node] = 1
            for adjNode in adj[node]:
                if visited[adjNode] == 0:
                    if dfs(adjNode, node):
                        return True
                elif adjNode != parent:
                    return True
            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True
        return False
