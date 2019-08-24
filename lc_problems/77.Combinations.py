from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []

        def backtrack(start=1, curr=[]):
            if len(curr) == k:
                out.append(curr[:])
            else:
                for i in range(start, n + 1):
                    curr.append(i)
                    backtrack(i + 1, curr)
                    curr.pop()
        backtrack()
        return out

    def combine_optimized(self, n: int, k: int) -> List[List[int]]:
        out = [[]]

        def backtrack(start=1):
            if len(out[-1]) == k:
                out.append(out[-1][:])
            else:
                for i in range(start, n + 1):
                    out[-1].append(i)
                    backtrack(i + 1, out[-1])
                    out[-1].pop()
        backtrack()
        return out
