class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        out = 0
        for _ in range(32):
            out += n & 1
            n >>= 1
        return out
    def hammingWeight_genius(self, n):
        out = 0
        while n:
            n = (n-1)&n
            out += 1
        return out
            
