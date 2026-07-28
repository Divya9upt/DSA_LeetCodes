class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        n = len(s)
        cnt = Counter(s)
        
        half_chars = []
        mid_char = ''
        for c in sorted(cnt.keys()):
            freq = cnt[c]
            if freq % 2 == 1:
                mid_char = c
            half_chars.append(c * (freq // 2))
        
        half = ''.join(half_chars)
        return half + mid_char + half[::-1]