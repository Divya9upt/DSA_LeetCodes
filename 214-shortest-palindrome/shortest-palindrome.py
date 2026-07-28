class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        rev = s[::-1]
        combined = s + '#' + rev
        n = len(combined)
        
        fail = [0] * n
        for i in range(1, n):
            j = fail[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = fail[j - 1]
            if combined[i] == combined[j]:
                j += 1
            fail[i] = j
        longest_palindrome_prefix_len = fail[-1]
        to_add = rev[:len(s) - longest_palindrome_prefix_len]
        
        return to_add + s