class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        curr = []

        def backtrack(start=0):
            out.append(curr[:])
            for i in range(start, len(nums)):
                if i == start or nums[i] != nums[i-1]:
                    curr.append(nums[i])
                    backtrack(i+1)
                    curr.pop()
        backtrack()
        return out
