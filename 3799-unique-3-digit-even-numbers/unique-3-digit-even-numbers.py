from typing import List
from itertools import permutations


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        valid = set()
        for p in set(permutations(digits, 3)):
            if p[0] != 0 and p[2] % 2 == 0:
                valid.add(p)
        return len(valid)