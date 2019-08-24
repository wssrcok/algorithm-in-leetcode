class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        while j - i > 1:
            m = i + (j - i) // 2
            # m will not be 0 or len(nums) - 1
            if nums[m-1] < nums[m] < nums[m+1]:
                i = m  # go to right
            elif nums[m-1] > nums[m] > nums[m+1]:
                j = m
            elif nums[m-1] > nums[m] < nums[m+1]:
                i = m
            else:
                return m
        return i if nums[i] > nums[j] else j
