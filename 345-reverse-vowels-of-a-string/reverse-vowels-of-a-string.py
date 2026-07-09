import re

class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        idx = [m.start() for m in re.finditer(r'[aeiouAEIOU]', s)]
        
        left, right = 0, len(idx) - 1
        while left < right:
            i, j = idx[left], idx[right]
            chars[i], chars[j] = chars[j], chars[i]
            left += 1
            right -= 1
        
        return ''.join(chars)