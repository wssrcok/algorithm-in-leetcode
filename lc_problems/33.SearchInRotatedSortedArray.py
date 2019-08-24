class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = i + (j - i) // 2
            if nums[m] == target:
                return m
            if nums[i] <= nums[m]:  # left is normal
                if nums[i] <= target < nums[m]:
                    j = m - 1
                else:
                    i = m + 1
            else:  # right is normal
                if nums[m] < target <= nums[j]:
                    i = m + 1
                else:
                    j = m - 1
        return -1
