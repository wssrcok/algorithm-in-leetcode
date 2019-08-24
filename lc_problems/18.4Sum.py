class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = 4
        if len(nums) < N:
            return []
        out = []
        nums.sort()
        def loop(n=N, start=0, t=target, curr=[]):
            if n == 2:
                for pair in self.twoSum(nums, start, t):
                    out.append(curr + pair)
            else:
                for i in range(start, len(nums) - (n-1)):
                    if i == start or nums[i] != nums[i-1]:
                        curr.append(nums[i])
                        loop(n-1, i + 1, t-nums[i], curr)
                        curr.pop()
        loop()
        return out

    def twoSum(self, nums: List[int], i: int, target: int) -> List[List[int]]:
        '''
        nums is sorted
        '''
        out = []
        j = len(nums) - 1
        while i < j:
            _sum = nums[i] + nums[j]
            if _sum > target:
                j -= 1
            elif _sum < target:
                i += 1
            else:
                out.append([nums[i], nums[j]])
                while i < j and nums[i] == nums[i+1]:
                    i += 1
                while i < j and nums[i] == nums[j-1]:
                    j -= 1
                i, j = i + 1, j - 1
        return out
