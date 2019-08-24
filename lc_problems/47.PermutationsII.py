from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        def backtrack(curr=[], digits=nums):
            if len(curr) == len(nums):
                out.append(curr.copy())
            else:
                for i, n in enumerate(digits):
                    if i > 0 and digits[i-1] == digits[i]:
                        continue
                    curr.append(n)
                    backtrack(curr, digits[:i] + digits[i+1:])
                    curr.pop()
        backtrack()
        return out

    def permuteUnique_with_swap(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        def backtrack(start=0):
            if start == len(nums):
                out.append(nums.copy())
            else:
                for i in range(start, len(nums)):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    nums[i], nums[start] = nums[start], nums[i]
                    backtrack(start + 1)
                    nums[i], nums[start] = nums[start], nums[i]
        backtrack()
        return out
