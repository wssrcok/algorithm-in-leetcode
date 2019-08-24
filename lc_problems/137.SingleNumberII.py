from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        states:
            00 -> 01 -> 10 -> 00
            our goal is to make state go back to zero using 
            bit manipulation when a bit appeared to be same 
            value for three times, when 0 appeared three 
            times, we can probably ignore it if we are not using `~`

            let's focus on 1 appeared three times:
            for digits[1], if digits[0] is 0, we just do xor
            with incoming 1s
            if digits[0] is 1, we stay at zero
            for digits[0], we xor it with 1 if next digits[1]
            is not 1, else stay at 0
        '''
        a, b = 0, 0
        for n in nums:
            b = (b ^ n) & ~a
            a = (a ^ n) & ~b
        return b

    def singleNumber_five(self, nums: List[int]) -> int:
        '''
        states:
            000 -> 001 -> 010 -> 011 -> 100 -> 000
        '''
        a,b,c=0,0,0
        for n in nums:
            b = b ^ (n & c)
            c = (n ^ c) & ~a
            a = (n ^ a) & ~c & ~b
        return c

    def singleNumber_seven(self, nums: List[int]) -> int:
        '''
        states:
            000 -> 001 -> 010 -> 011 -> 100 -> 101 -> 110 -> 000
        '''
        a,b,c = 1,0,1
        for n in nums:
            old_b = b
            b = (c&b) ^ n
            c = (n^c) & ~(a&old_b)
            a = (a^n) & ~b & ~c
            print(a,b,c)
        return c
solution = Solution()
print(solution.singleNumber_seven([3,0,3,3,3,3,3,3]))
    
