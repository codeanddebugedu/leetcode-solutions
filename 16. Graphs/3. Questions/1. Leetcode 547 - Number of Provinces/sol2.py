from typing import List

"""
Time Complexity: O(N) + O(V+2E), 
Where O(N) is for outer loop and inner loop runs in total a single DFS over entire graph, 
and we know DFS takes a time of O(V+2E). 

Space Complexity: O(N) + O(N),Space for recursion stack space and visited array.
"""


class Solution:
    def dfs(self, node: int, adj: List[List[int]], visited: List[int]):
        visited[node] = 1
        for neighbor in adj[node]:
            if visited[neighbor] == 0:
                self.dfs(neighbor, adj, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        totalNodes = len(isConnected)
        adj = [[] for _ in range(totalNodes)]

        # Convert adjacency matrix to adjacency list
        for i in range(totalNodes):
            for j in range(totalNodes):
                if isConnected[i][j] == 1 and i != j:
                    adj[i].append(j)

        visited = [0] * totalNodes
        count = 0

        # Count connected components using DFS
        for i in range(totalNodes):
            if visited[i] == 0:
                self.dfs(i, adj, visited)
                count += 1

        return count
