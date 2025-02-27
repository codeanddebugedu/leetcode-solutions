from collections import deque


class Solution:
    def topologicalSort(self, adj):
        V = len(adj)
        indegree = [0] * V
        for u in range(V):
            for v in adj[u]:
                indegree[v] += 1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        topo_order = []
        while q:
            node = q.popleft()
            topo_order.append(node)
            for nxt in adj[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return topo_order
