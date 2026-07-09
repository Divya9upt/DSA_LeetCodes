class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        b = bytearray(s, 'ascii')
        n = len(b)
        
        for start in range(0, n, 2 * k):
            end = min(start + k, n)
            b[start:end] = b[start:end][::-1]
        
        return b.decode('ascii')