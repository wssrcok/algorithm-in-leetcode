class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def next(n):
            return nums[n]
        slow = fast = nums[0]
        # gaurenteed to have a cycle
        while True:
            slow, fast = next(slow), next(next(fast))
            if slow == fast: break
        slow2 = nums[0]
        while slow != slow2:
            slow, slow2 = next(slow), next(slow2)
        return slow
