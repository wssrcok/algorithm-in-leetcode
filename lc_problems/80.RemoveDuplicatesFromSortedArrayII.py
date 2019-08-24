class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        i = 2
        prev = nums[1]
        for j in range(2, len(nums)):
            two_before = nums[j-2]
            if j == i + 1:  # when j is i + 1, it will check nums[j-2] which might be changed from original value since it is before i. so we store it's previous value. However, this approach costs O(k-1) space when it's generalized to k duplicates. See below to get O(1) space
                two_before = prev
            if two_before != nums[j]:
                prev = nums[i]
                nums[i] = nums[j]
                i += 1
        return i

    def removeDuplicates_k(self, nums: List[int]) -> int:
        k = 2
        if len(nums) <= k:
            return len(nums)
        count = 0
        i = 0
        for j in range(len(nums)):
            if j == 0 or nums[j] != nums[j-1]:
                count = 1
            else:
                count += 1
            if count <= k:
                nums[i] = nums[j]
                i += 1
        return i
