class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        averages = set()
        
        for i in range(n // 2):
            avg = (nums[i] + nums[n - 1 - i]) / 2
            averages.add(avg)
        
        return len(averages)