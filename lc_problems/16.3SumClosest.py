class Solution:
    # can I use Set for this question?
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            raise Exception("length of nums should at lease be 3")
        nums.sort()
        out = sum(nums[:3])
        distance = abs(out - target)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums) - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum < target:
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                elif _sum > target:
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                else:
                    return target
                if abs(target - _sum) < distance:
                    distance = abs(target - _sum)
                    out = _sum
        return out
