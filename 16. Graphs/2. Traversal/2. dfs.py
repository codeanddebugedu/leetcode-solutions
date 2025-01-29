"""
Time Complexity: For an undirected graph, O(N) + O(2E), 
For a directed graph, O(N) + O(E), Because for every node we are calling the recursive function once, 
the time taken is O(N) and 2E is for total degrees as we traverse for all adjacent nodes.

Space Complexity: O(3N) ~ O(N), Space for dfs stack space, visited array and an adjacency list.
"""


class Solution:
    def dfs(self, node, visited, result, adj):
        visited[node] = 1
        result.append(node)
        for node in adj[node]:
            if visited[node] != 1:
                self.dfs(node, visited, result, adj)

    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        result = []
        visited = [0] * (V + 1)
        self.dfs(1, visited, result, adj)
        return result


obj = Solution()
x = obj.dfsOfGraph(5, [[], [2, 3], [1, 4, 5], [1, 4], [2, 3, 5], [2, 4]])
print(x)
