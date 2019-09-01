class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        m1, m2 = {}, {}
        A = B = 0
        for s, g in zip(secret, guess):
            if s == g:
                A += 1
            else:
                if s in m2 and m2[s] > 0:
                    m2[s] -= 1
                    B += 1
                else:
                    m2[s] = m2.get(s, 0) + 1
                if g in m1 and m1[g] > 0:
                    m1[g] -= 1
                    B += 1
                else:
                    m1[g] = m1.get(g, 0) + 1
        return A+'A'+B+'B'

            
