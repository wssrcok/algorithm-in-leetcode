from functools import reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = reduce(operator.xor, nums)
        xor &= -xor
        out = [0,0]
        for n in nums:
            if n&xor:
                out[0] ^= n
            else:
                out[1] ^= n
        return out
