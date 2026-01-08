class Solution:
    def isCycle(self, V, edges):
        parent = [-1] * V

        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return True
            parent[px] = py
            return False

        for u, v in edges:
            if union(u, v):
                return True

        return False
