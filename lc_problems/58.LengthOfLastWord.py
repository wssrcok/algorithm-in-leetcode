class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        if not s:
            return 0
        i = len(s) - 1
        while s[i] != ' ':
            i -= 1
        if i == 0:
            return len(s)
        return len(s) - i - 1
