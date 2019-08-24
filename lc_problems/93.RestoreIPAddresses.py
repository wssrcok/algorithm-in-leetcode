class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        out = []
        def backtrack(start=0, curr='', dots=3):
            if dots < 0:
                if start == len(s):
                    out.append(curr[:-1])
            elif start < len(s) and dots < len(s) - start <= (dots + 1) * 3:
                backtrack(start + 1, curr + s[start:start+1] + '.', dots-1)
                if s[start] != '0' and start + 2 <= len(s):
                    backtrack(start + 2, curr + s[start:start+2] + '.', dots-1)
                if s[start] != '0' and start + 3 <= len(s) and int(s[start:start+3]) <= 255:
                    backtrack(start + 3, curr + s[start:start+3] + '.', dots-1)
        backtrack()
        return out
    
