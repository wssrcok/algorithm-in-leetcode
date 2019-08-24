class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # sum up all, divide by K
        _sum = sum(nums)
        val = _sum // k
        if val < 1 or _sum % k != 0 or max(nums) > val:
            return False
        nums.sort()
        while nums and nums[-1] == val:
            k -= 1
            nums.pop()

        def backtrack(groups=[0] * k):
            if not nums:
                return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v > val:
                    continue  # try next group
                groups[i] += v  # add to group and adding next
                if backtrack(groups): return True
                groups[i] -= v
                if group == 0: break
            nums.append(v)
            return False
                
                
        return backtrack()
