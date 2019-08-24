class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        i = 0
        while c and i < len(digits):
            digits[~i] += 1
            c = digits[~i] // 10
            digits[~i] %= 10
            i += 1
        return ([1] if c else []) + digits
