class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = 0
        for i, v in enumerate(reversed(citations)):
            if v <= i:
                break
            res += 1
        return res

    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        if l == 0:
            return 0
        if l == 1:
            return int(citations[0] > 0)
        i, j = 0, l - 1
        while j - i > 1:
            m = i + (j - i) // 2
            if citations[m] >= l - m:
                j = m
            else:
                i = m
        if citations[i] >= l - i:
            return l - i
        if citations[j] >= l - j:
            return l - j
        return 0
