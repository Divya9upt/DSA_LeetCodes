from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start: int):
            if start == len(nums):
                result.append(nums[:])   # make a copy
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # choose
                backtrack(start + 1)                         # explore
                nums[start], nums[i] = nums[i], nums[start]  # un-choose (backtrack)
        
        backtrack(0)
        return result
