class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        r, c = len(matrix), len(matrix[0])
        i, j = 0, r * c - 1
        while i <= j:
            m = i + (j - i) // 2
            val = matrix[m//c][m%c]
            if val == target:
                return True
            if val < target:
                i = m + 1
            else:
                j = m - 1
        return False
            
