class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=r=0
        m = collections.Counter(t)
        se = set(m.keys())
        i, j = -1, len(s)
        while r < len(s):
            while r < len(s) and se:
                if s[r] in m:
                    m[s[r]] -= 1
                    if m[s[r]] == 0:
                        se.remove(s[r])
                r += 1
            while l <= r and not se:
                if s[l] in m:
                    m[s[r]] += 1
                    if m[s[r]] == 1:
                        se.add(s[r])
                l += 1
            if l - r < j - i:
                i, j = l, r
        return s[i:j]
