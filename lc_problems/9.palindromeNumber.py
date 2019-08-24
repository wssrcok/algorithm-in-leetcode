class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        r = 0
        xx = x
        while xx:
            r = r * 10 + xx % 10
            xx //= 10
        return r == x
