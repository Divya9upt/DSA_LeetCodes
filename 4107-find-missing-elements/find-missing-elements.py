class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low , high = min(nums),max (nums)
        present=set(nums)
        return [x for x in range (low , high+1) if x not in present] 