class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        odd_chars = [i for i in range(26) if cnt[i] % 2 == 1]
        if n % 2 == 0:
            if odd_chars:
                return ""
        else:
            if len(odd_chars) != 1:
                return ""

        m = n // 2
        half = [cnt[i] // 2 for i in range(26)]
        mid_char = chr(odd_chars[0] + 97) if n % 2 == 1 else None

        T1 = target[:m]

        pools = [half[:]]
        current = half[:]
        L = 0
        for i in range(m):
            c = ord(T1[i]) - 97
            if current[c] > 0:
                current[c] -= 1
                pools.append(current[:])
                L += 1
            else:
                break

        def build_from_H(Hlist):
            Hstr = ''.join(Hlist)
            if n % 2 == 1:
                return Hstr + mid_char + Hstr[::-1]
            return Hstr + Hstr[::-1]

        if L == m:
            P1 = build_from_H(list(T1))
            if P1 > target:
                return P1

        j_max = L if L < m else m - 1
        for j in range(j_max, -1, -1):
            pool_j = pools[j]
            tc = ord(T1[j]) - 97
            found = -1
            for c in range(tc + 1, 26):
                if pool_j[c] > 0:
                    found = c
                    break
            if found == -1:
                continue

            leftover = pool_j[:]
            leftover[found] -= 1
            rest = []
            for c in range(26):
                if leftover[c]:
                    rest.extend([chr(c + 97)] * leftover[c])

            H2 = list(T1[:j]) + [chr(found + 97)] + rest
            return build_from_H(H2)

        return ""