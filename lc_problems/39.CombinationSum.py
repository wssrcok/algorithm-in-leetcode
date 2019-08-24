class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        def backtrack(start=0, curr=[], t=target):
            if t == 0:
                out.append(curr.copy())
            elif t > 0:
                for i in range(start, len(candidates)):
                    curr.append(candidates[i])
                    backtrack(i, curr, t-candidates[i])
                    curr.pop()
        return out
