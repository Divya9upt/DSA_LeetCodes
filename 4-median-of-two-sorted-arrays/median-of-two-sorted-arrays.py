class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        
        i, j = 0, 0
        prev, curr = 0, 0
        for count in range(half + 1):
            prev = curr
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
        
        if total % 2 == 1:
            return float(curr)
        else:
            return (prev + curr) / 2.0