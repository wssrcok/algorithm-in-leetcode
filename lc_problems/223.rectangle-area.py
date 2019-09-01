#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area = abs(A-C)*abs(B-D) + abs(E-G)*abs(F-H)
        overlap = max(0, min(C, G) - max(A, E)) * max(0, min(D, H) - max(B, F))
        return area - overlap


