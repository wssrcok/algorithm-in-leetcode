class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        visited = set()
        out = 0
        for n in num_set:
            if n not in visited:
                visited.add(n)
                length = 1
                left = n - 1
                while left in num_set:
                    length += 1
                    visited.add(left)
                    left -= 1
                right = n + 1
                while right in num_set:
                    length += 1
                    visited.add(right)
                    right += 1
                out = max(length, out)
        return out
