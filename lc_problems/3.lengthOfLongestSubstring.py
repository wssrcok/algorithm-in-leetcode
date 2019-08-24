def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
    out = left = right = 0
    d = {}
    while right < len(s):
        if s[right] in d:
            out = max(out, right - left)
            for i in range(left, d[s[right]] + 1):
                del d[s[i]]
            left = i + 1
        d[s[right]] = right 
        right += 1
    out = max(len(s) - left, out)
    return out
