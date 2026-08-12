from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        best = 0
        for right, x in enumerate(nums):
            count[x] += 1
            while count[x] > k:
                count[nums[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best