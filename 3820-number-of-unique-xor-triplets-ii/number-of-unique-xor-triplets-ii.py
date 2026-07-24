from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique = list(set(nums))
        
        # Step 1: all pairwise XORs (covers picking 2 elements, with repetition)
        pair_xors = set()
        for a in unique:
            for b in unique:
                pair_xors.add(a ^ b)
        
        # Step 2: XOR that set with every unique value to get all triple XORs
        result = set()
        for p in pair_xors:
            for a in unique:
                result.add(p ^ a)
        
        return len(result)