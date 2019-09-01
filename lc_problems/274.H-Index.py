class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        res = 0
        for i, v in enumerate(citations):
            if v > i:
                res += 1
            else:
                break
        return res

