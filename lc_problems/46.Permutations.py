from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []

        def backtrack(my_set=set(nums), curr=[]):
            if len(curr) == len(nums):
                out.append(curr.copy())
            else:
                for n in my_set.copy():
                    my_set.remove(n)
                    curr.append(n)
                    backtrack(my_set, curr)
                    curr.pop()
                    my_set.add(n)
        backtrack()
        return out

    def permute_using_swap(self, nums: List[int]) -> List[List[int]]:
        out = []

        def backtrack(start=0):
            if start == len(nums):
                out.append(nums.copy())
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
        backtrack()
        return out


solution = Solution()
for perm in solution.permute([1,2,3,4]):
    print(perm)
