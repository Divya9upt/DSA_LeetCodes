import re
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            re.compile('[qwertyuiopQWERTYUIOP]*$'),
            re.compile('[asdfghjklASDFGHJKL]*$'),
            re.compile('[zxcvbnmZXCVBNM]*$')
        ]
        return [w for w in words if any(row.match(w) for row in rows)]