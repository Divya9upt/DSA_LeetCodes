class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        cur=odd=even=res=0
        for i in arr:
            cur+=i
            if cur%2==1:
                res+=even+1
                odd+=1
            else:
                res+=odd
                even+=1
        return res%(10**9+7)