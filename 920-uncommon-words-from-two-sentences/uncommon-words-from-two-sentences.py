
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
        freq = Counter(words)


        return [word for word in freq if freq[word] == 1]
