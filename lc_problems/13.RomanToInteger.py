class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'M':1000, 'D':500, 
             'C':100, 'L':50,
             'X':10, 'V':5, 'I':1}
        out = 0
        for i in range(len(s)):
            if i < len(s) - 1 and d[s[i+1]] > d[s[[i]]:
                out -= d[s[i]]
            else:
                out += d[s[i]]
        return out
