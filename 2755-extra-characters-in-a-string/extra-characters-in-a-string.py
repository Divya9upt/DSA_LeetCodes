class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        di = {}
        end = "#"

        # Build trie
        for word in dictionary:
            t = di
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t[end] = True

        n = len(s)
        dpt = [float("inf")] * (n + 1)
        dpt[0] = 0

        for i in range(n):
            dpt[i + 1] = min(dpt[i + 1], dpt[i] + 1)

            t = di
            for j in range(i, n):
                if s[j] not in t:
                    break

                t = t[s[j]]

                if end in t:
                    dpt[j + 1] = min(dpt[j + 1], dpt[i])

        return dpt[n]