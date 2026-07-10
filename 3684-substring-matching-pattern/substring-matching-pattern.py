class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        star = p.index('*')
        prefix, suffix = p[:star], p[star + 1:]
        n = len(s)

        for i in range(n + 1):
            if not s.startswith(prefix, i):
                continue
            start_of_middle = i + len(prefix)
            # j must leave room for suffix to NOT overlap with prefix's matched region
            for j in range(start_of_middle + len(suffix), n + 1):
                if s.endswith(suffix, start_of_middle, j):
                    return True
        return False