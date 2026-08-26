class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        count = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                count += 1
            while count == k:
                while left <= right and s[left] == '0':
                    left += 1

                current = s[left:right + 1]

                if ans == "":
                    ans = current
                elif len(current) < len(ans):
                    ans = current
                elif len(current) == len(ans) and current < ans:
                    ans = current
                if s[left] == '1':
                    count -= 1

                left += 1

        return ans