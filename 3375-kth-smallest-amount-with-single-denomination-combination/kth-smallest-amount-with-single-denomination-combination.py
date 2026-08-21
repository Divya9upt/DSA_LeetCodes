from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        def count_le(x: int) -> int:
            """Count how many amounts <= x are achievable (union of multiples)."""
            total = 0
            # iterate over all non-empty subsets of coins
            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                overflow = False
                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        lcm = lcm * coins[i] // gcd(lcm, coins[i])
                        if lcm > x:
                            overflow = True
                            break
                if overflow:
                    continue
                if bits % 2 == 1:
                    total += x // lcm
                else:
                    total -= x // lcm
            return total
        
        lo, hi = 1, k * min(coins)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        
        return lo