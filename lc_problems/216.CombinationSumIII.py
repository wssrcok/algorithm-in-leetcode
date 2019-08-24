class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > sum(range(1, 10)) or k > 9 or k > n:
            return []
        out = []
        def backtrack(start=1, curr=[], t=n):
            if len(curr) == k and t == 0:
                out.append(curr.copy())
            elif len(curr) < k and t > 0:
                for i in range(start, 10):
                    curr.append(i)
                    backtrack(i+1, curr, t-i)
                    curr.pop()
        backtrack()
        return out
