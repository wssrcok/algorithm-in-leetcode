class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 2 and 5 creates a zero
        # 4 and 25 creates two zero
        # 8 and 125 creates zeros
        # 2^n and 5^n creates zeros
        # once you reach 5, you can pair it with a 2 before to get a zero
        # once you reach 25, you can pair it with a for before to get 2 zeros
        #  n,  zeros 
        #  5     1
        #  10    2
        #  15    3
        #  20    4
        #  25    6   2 tens + 2  fives + 1 25s
        # if less than 25, result is n // 5
        # if less than 125, result is n // 5 + n // 25
        out = 0
        while n:
            n //= 5
            out += n
        return out
