class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest = len(nums) - 1
        for i in reversed(range(len(nums)-1)):
            if i + nums[i] >= dest:
                dest = i
        return dest == 0
