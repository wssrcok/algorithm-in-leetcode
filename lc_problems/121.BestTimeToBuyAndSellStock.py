class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        _min = prices[0]
        out = 0
        for p in prices[1:]:
            out, _min = max(out, p-_min), min(_min, p)
        return out

