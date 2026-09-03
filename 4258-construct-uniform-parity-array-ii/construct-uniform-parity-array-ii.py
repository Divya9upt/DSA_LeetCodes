class Solution:
    def uniformArray(self, nums1):
        has_odd = False
        has_even = False
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2 == 0:
                has_even = True
                min_even = min(min_even, x)
            else:
                has_odd = True
                min_odd = min(min_odd, x)

        if not has_odd or not has_even:
            return True
        return min_odd < min_even