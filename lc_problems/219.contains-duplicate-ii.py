#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        se = set(nums[:k+1])
        if len(se) < len(nums[:k+1]):
            return True
        for i in range(k+1, len(nums)):
            se.remove(nums[i-k-1])
            se.add(nums[i])
            if len(se) < k + 1:
                return True
        return False

