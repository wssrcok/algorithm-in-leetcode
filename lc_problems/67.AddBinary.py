class Solution:
    def addBinary(self, a: str, b: str) -> str:
        out = ''
        C = 0
        for i in range(max(len(a), len(b))):
            A = int(a[~i]) if i < len(a) else 0 
            B = int(b[~i]) if i < len(b) else 0
            out = str(A ^ B ^ C) + out
            C = int(A + B + C > 1)
        return ('1' if C else '') + out
        
