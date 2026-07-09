class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        chars = list(s)
        # Collect indices of vowels only once
        idx = [i for i, c in enumerate(chars) if c in vowels]
        
        left, right = 0, len(idx) - 1
        while left < right:
            i, j = idx[left], idx[right]
            chars[i], chars[j] = chars[j], chars[i]
            left += 1
            right -= 1
        
        return ''.join(chars)