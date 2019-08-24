class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def brutalforce():
            j = 0
            _max = nums[0]
            while j < len(nums):
                for i in range(j+1):
                    p = 1
                    for n in nums[i:j+1]:
                        p *= n
                    _max = max(_max, p)
                j += 1
            return _max

        def dynamicProgramming():
            out = nums[0]
            _min = _max = 1
            for n in nums:
                if n != 0:
                    _max = max(_min * n, _max) if n < 0 else _max * n
                    _min = min(_max * n, _min) if n < 0 else _min * n
                else:
                    out = max(out, _max)
                    _min = _max = 1
            return out



            
