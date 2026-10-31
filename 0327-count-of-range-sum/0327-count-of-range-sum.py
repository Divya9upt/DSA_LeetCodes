
class Solution:
    def countRangeSum(self, nums, lower, upper):
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        def merge_sort(left, right):
            if right - left <= 1:
                return 0

            mid = (left + right) // 2

            count = merge_sort(left, mid)
            count += merge_sort(mid, right)

            low = high = mid

            for i in range(left, mid):
                while low < right and prefix[low] - prefix[i] < lower:
                    low += 1

                while high < right and prefix[high] - prefix[i] <= upper:
                    high += 1

                count += high - low

            # Merge two sorted halves
            temp = []
            i, j = left, mid

            while i < mid and j < right:
                if prefix[i] <= prefix[j]:
                    temp.append(prefix[i])
                    i += 1
                else:
                    temp.append(prefix[j])
                    j += 1

            temp.extend(prefix[i:mid])
            temp.extend(prefix[j:right])

            prefix[left:right] = temp

            return count

        return merge_sort(0, len(prefix))
