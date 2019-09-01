#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        '''
        set up buckets in map
        for every incoming number such as 10
        if our bucket size t is 5, then 10 should be in bucket index 1 (second bucket)
        we can get the number by 10 / t + 1 
        so it two numbers are in the same bucket,
        their difference must be less than or equal to t
        and if neighbor buckets exist. we just need to find
        difference between incoming and neibering number buckets <= t
        '''
        if t < 0 or k < 0:
            return False
        buckets = {}
        for i, n in enumerate(nums):
            if len(buckets) == k + 1:
                del buckets[nums[i-k-1]//(t+1)]
            pos = n // (t+1)
            if pos in buckets:
                return True
            if pos - 1 in buckets and n - buckets[pos-1] <= t:
                return True
            if pos + 1 in buckets and buckets[pos+1] - n <= t:
                return True
            buckets[pos] = n
        return False

