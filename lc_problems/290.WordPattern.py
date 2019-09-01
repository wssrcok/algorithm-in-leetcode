class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        p = list(pattern)
        s = str.split()
        return len(set(p)) == len(set(s)) == len(set(zip(p,s)) and len(p) == len(s)
