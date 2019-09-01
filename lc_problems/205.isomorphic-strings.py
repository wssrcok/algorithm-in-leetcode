#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
        # number of distinct c in s is equal to distinct c in t
        # 
