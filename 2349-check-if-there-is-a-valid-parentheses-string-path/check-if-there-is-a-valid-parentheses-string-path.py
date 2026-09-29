from functools import cache
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        @cache
        def dfs(i, j, k):
            k += 1 if grid[i][j] == '(' else -1
            if k < 0 or k > m - i + n - j - 1:
                return False
            if i == m - 1 and j == n - 1:
                return k == 0
            if i + 1 < m and dfs(i + 1, j, k):
                return True
            if j + 1 < n and dfs(i, j + 1, k):
                return True
            return False
        return dfs(0, 0, 0)