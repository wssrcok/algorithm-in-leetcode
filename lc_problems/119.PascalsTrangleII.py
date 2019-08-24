class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        prev = self.getRow(rowIndex - 1)
        l = len(prev) + 1
        curr = [1] * l
        for i in range(l - 2):
            curr[i+1] = prev[i] + prev[i+1]
        return curr
