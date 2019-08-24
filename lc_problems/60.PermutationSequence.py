from pysnooper import snoop

class Solution:
    @snoop()
    def getPermutation(self, n: int, k: int) -> str:
        elems = [i for i in range(1, n+1)]
        out = ''
        block_size = 1
        for i in range(2, n+1):
            block_size *= i
        for x in range(n, 0, -1):
            block_size //= x
            block_index = (k-1) // block_size
            offset = ((k-1) % block_size) + 1
            k = offset
            out += str(elems[block_index])
            elems.pop(block_index)  # worst case time complexity O(9)
        return out

solution = Solution()
solution.getPermutation(4, 9)
