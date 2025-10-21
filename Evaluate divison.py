from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (A, B), val in zip(equations, values):
            graph[A][B] = val
            graph[B][A] = 1 / val

        def dfs(start, end, visited):
            if start not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, weight in graph[start].items():
                if neighbor in visited:
                    continue
                res = dfs(neighbor, end, visited)
                if res != -1.0:
                    return weight * res
            return -1.0

        results = []
        for X, Y in queries:
            results.append(dfs(X, Y, set()))
        return results
