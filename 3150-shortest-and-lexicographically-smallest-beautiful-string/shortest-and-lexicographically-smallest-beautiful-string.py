class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        count = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                count += 1

            # Window mein exactly k ones
            while count == k:
                # Left ke unnecessary zero hatao
                while left <= right and s[left] == '0':
                    left += 1

                current = s[left:right + 1]

                if ans == "":
                    ans = current
                elif len(current) < len(ans):
                    ans = current
                elif len(current) == len(ans) and current < ans:
                    ans = current

                # Next possible window ke liye left wala 1 hatao
                if s[left] == '1':
                    count -= 1

                left += 1

        return ans