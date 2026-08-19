class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        actual_sum = sum(nums)
        actual_sq_sum = sum(x * x for x in nums)
        
        expected_sum = n * (n + 1) // 2
        expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6
        
        diff = actual_sum - expected_sum
    
        sq_diff = actual_sq_sum - expected_sq_sum
        
        total = sq_diff // diff
        
        duplicate = (diff + total) // 2
        missing = total - duplicate
        
        return [duplicate, missing]

        #solved