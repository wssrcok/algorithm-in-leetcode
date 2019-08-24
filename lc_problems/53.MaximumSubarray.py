class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        _sum = 0
        _max = nums[0]
        for n in nums:
            _sum += n
            _max = max(_sum, _max)
            if _sum < 0:
                _sum = 0
        return _max
