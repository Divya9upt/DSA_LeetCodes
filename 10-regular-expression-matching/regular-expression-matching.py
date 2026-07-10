from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and p[j] in (s[i], '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                # zero occurrences OR one-plus occurrences
                return dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                return first_match and dp(i + 1, j + 1)

        return dp(0, 0)