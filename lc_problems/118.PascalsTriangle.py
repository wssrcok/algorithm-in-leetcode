class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = []
        for l in range(numRows):
            curr = [1] * l
            for i in range(l-2):
                curr[i+1] = out[-1][i] + out[-1][i+1]
            out.append(curr)
        return out

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        prev = self.generate(numRows-1)
        l = len(prev[-1]) if prev else 0
        curr = [1] * (l + 1)
        for i in range(l - 1):
            curr[i+1] = prev[-1][i] + prev[-1][i+1]
        return prev + [curr] 
