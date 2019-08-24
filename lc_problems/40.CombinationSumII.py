class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()
        def backtrack(start=0, curr=[], t=target):
            if t == 0:
                out.append(curr.copy())
            elif t > 0:
                for i in range(start, len(candidates)):
                    if i == start or candidates[i] != candidates[i-1]:
                        curr.append(candidates[i])
                        backtrack(i + 1, curr, t - candidates[i])
                        curr.pop()
        backtrack()
        return out 
