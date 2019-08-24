class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = two = three = 0
        for n in nums:
            old_one = one
            one = max(two + n, three + n)
            two, three = old_one, two
        return max(two + n, three + n)
