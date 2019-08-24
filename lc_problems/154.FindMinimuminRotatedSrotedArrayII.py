class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        if nums[i] < num[j]:
            return nums[i]
        while j - i > 1:
            m = i + (j - i) // 2
            while j > m and nums[j] == nums[m]:
                j -= 1                
            if nums[m] <= nums[j]:
                j = m
            else:
                i = m
        return nums[j]

