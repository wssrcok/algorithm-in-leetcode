class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}
        for i, c in enumerate(keyboard):
            d[c] = i
        out = 0 
        prev = 0
        for w in word:
            out += abs(d[w] - prev)
            prev = d[w]
        return out
            
            
