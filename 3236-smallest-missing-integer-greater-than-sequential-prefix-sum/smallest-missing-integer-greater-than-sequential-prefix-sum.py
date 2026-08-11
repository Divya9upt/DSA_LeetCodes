class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        n = len(nums)
       
        i = 0
        while i + 1 < n and nums[i + 1] == nums[i] + 1:
            i += 1
        total = sum(nums[:i + 1])
        num_set = set(nums)
        while total in num_set:
            total += 1
        return total