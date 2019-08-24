class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        i, j = 0, len(nums) - 1
        while i <= j:
            m = i + (j - i) // 2
            if nums[m] == target and (m == 0 or nums[m-1] < nums[m]):
                break 
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        if i > j:
            return [-1, -1]
        i, j = m, len(nums) - 1
        left = i
        while i <= j:
            m = i + (j - i) // 2
            if nums[m] == target and (m == len(nums) - 1 or nums[m+1] > nums[m]):
                return [left, m] 
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        raise Exception("shouldn't reach here")
