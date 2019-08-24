class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        for i in reversed(range(len(nums))):
            if i == 0:
                nums.reverse()
                return
            if nums[i] > nums[i-1]:
                break
        before = nums[i-1]
        ii = i
        while ii < len(nums) - 1 and nums[ii+1] > nums[i-1]:
            ii += 1
        nums[i-1], nums[ii] = nums[ii], nums[i-1]
        nums[i:] = list(reversed(nums[i:]))
