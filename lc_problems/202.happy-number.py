#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s:
            s.add(n)
            then = 0
            while n:
                then += (n % 10)**2
                n //= 10
            n = then
            if n == 1:
                return True
        return False



