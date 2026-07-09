class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        n = len(chars)
        
        for start in range(0, n, 2 * k):
            end = min(start + k, n)
            chars[start:end] = chars[start:end][::-1]
        
        return ''.join(chars)