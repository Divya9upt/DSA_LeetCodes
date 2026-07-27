class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= k:
                seen.add(nums[i])
            if len(seen) == k:
                return len(nums) - i
        return -1  # not reachable per constraints