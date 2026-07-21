from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer for the position of the next non-zero element
        last_non_zero = 0
        
        # Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1
        
        # Fill the rest with zeros
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0

# Example usage:
nums = [0, 1, 0, 3, 12]
solution = Solution()
solution.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
