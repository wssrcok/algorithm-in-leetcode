from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return str(int(''.join(sorted(map(str, nums), key=cmp_to_key(lambda a, b: cmp(b+a,a+b))))))
