from typing import List, Optional
from collections import defaultdict, deque

class Solution:
    def addEdge(self, u: int, v: int) -> None:
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfsUtil(self, node: int, visited: set, path: list) -> bool:
        if node in path:
            return False
        if node in visited:
            return True

        visited.add(node)
        path.append(node)

        for neighbor in self.graph[node]:
            if not self.dfsUtil(neighbor, visited, path):
                return False

        path.pop()
        visited.remove(node)
        return True

    def courseSchedule(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in prerequisites:
            self.addEdge(x, y)

        visited = set()
        path = []

        for i in range(numCourses):
            if not self.dfsUtil(i, visited, path):
                return False

        return True