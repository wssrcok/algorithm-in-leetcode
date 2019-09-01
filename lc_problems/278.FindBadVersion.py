# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i <= j:
            m = i + (j - i) // 2
            if isBadVersion(m):
                if m == 1 or not isBadversion(m-1):
                    return m
                j = m - 1
            else:
                i = m + 1

            
