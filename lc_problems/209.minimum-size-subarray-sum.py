#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        cur = 0
        res = len(nums) + 1
        for j in range(len(nums)):
            cur += nums[j]
            while cur >= s:
                cur -= nums[i]
                i += 1
                res = min(j - i + 2, res)
        return res if res <= len(nums) else 0


