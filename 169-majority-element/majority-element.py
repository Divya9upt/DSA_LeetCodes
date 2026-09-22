class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        result,count=0,0

        for num in nums:
            if count==0:
                result=num
            count+=(1 if num==result else -1)
        return result