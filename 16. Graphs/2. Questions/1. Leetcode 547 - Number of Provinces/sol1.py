from typing import List

# Without creating List


class Solution:
    def dfs(self, node, adj, visited):
        visited[node] = 1
        for n in range(len(adj)):
            if adj[node][n] == 1 and visited[n] == 0:
                self.dfs(n, adj, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        totalNodes = len(isConnected)
        visited = [0] * totalNodes
        count = 0
        for i in range(totalNodes):
            if visited[i] == 0:
                self.dfs(i, isConnected, visited)
                count += 1
        return count
