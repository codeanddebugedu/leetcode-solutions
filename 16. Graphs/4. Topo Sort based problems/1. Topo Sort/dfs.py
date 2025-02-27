class Solution:

    def topologicalSort(self, adj):
        V = len(adj)
        visited = [False] * V
        order = []

        def dfs(u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)
            order.append(u)

        for i in range(V):
            if not visited[i]:
                dfs(i)
        return order[::-1]
