class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m, n = m - 1, n - 1
        for i in range(len(nums1)):
            M = nums1[m] if m >= 0 else float('-inf')
            N = nums2[n] if n >= 0 else float('-inf')
            if M > N:
                nums1[~i] = M
                m -= 1
            else:
                nums1[~i] = N
                n -= 1
