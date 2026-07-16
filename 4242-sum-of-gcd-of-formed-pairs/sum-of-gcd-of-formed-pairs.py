import math
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefixGcd = []
        mx = 0
        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(math.gcd(num, mx))
        prefixGcd.sort()
        
        total = 0
        left, right = 0, n - 1
        while left < right:
            total += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        
        return total
