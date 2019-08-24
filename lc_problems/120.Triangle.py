class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        prev = triangle[-1]
        for ls in reversed(triangle[:-1]):
            for i in range(len(ls)):
                ls[i] += min(prev[i], prev[i+1])
            prev = ls
        return prev[0]
