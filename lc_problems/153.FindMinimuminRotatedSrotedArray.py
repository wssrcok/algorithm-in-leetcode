class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            m = i + (j - i) // 2
            n = nums[m]
            if m == 0:
                return min(n, nums[m+1])
            if nums[m-1] > n:
                return n
            if nums[i] > n:
                j = m - 1
            elif nums[j] < n:
                i = m + 1
            else:
                return nums[i]
        return nums[i] 

