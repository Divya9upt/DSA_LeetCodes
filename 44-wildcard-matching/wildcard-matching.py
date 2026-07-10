class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        star_idx = -1      # last position of '*' seen in p
        match_idx = 0       # position in s where that '*' last matched up to

        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                # direct character match
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                # record star position, tentatively match zero characters
                star_idx = j
                match_idx = i
                j += 1
            elif star_idx != -1:
                # backtrack: let '*' absorb one more character
                j = star_idx + 1
                match_idx += 1
                i = match_idx
            else:
                # no match, and no '*' to fall back on
                return False

        # consume any remaining '*' in p (they can match empty)
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)