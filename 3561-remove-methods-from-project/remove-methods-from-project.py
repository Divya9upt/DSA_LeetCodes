from collections import defaultdict, deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)
        visited = {k}
        queue = deque([k])
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        
        for a, b in invocations:
            if b in visited and a not in visited:
                return list(range(n))
        return [i for i in range(n) if i not in visited]