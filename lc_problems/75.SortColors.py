class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums) - 1
        m = 0
        while m <= j:
            if nums[m] == 0:
                nums[i], nums[m] = nums[m], nums[i]
                i += 1
            elif nums[m] == 2:
                nums[j], nums[m] = nums[m], nums[j]
                j -= 1
            if nums[m] != 2:
                m += 1
