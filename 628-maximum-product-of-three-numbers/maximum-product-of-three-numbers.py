class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        
        for n in nums:
            # update top 3 max
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n > max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n
            
            # update bottom 2 min
            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n
        
        return max(max1 * max2 * max3, min1 * min2 * max1)
        