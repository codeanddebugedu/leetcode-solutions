from collections import deque


class Solution:
    def isCyclic(self, V, adj):

        indegree = [0] * V
        for i in range(V):
            for v in adj[i]:
                indegree[v] += 1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        count = 0
        while q:
            u = q.popleft()
            count += 1
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return count < V  # True if there's a cycle, False otherwise
