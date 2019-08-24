class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        out = ''
        mins = len(strs[0])
        for s in strs:
            mins = min(len(s), mins)
        for i in range(0, mins):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j-1][i]:
                    return out
            out += strs[0][i]
        return out 
