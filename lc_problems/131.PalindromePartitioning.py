class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []
        
        def isPalindrome(strr):
            return strr == strr[::-1]

        def backtrack(curr=[], st=s):
            if st == '':
                out.append(curr[:])
            else:
                for i in range(1, len(st)+1):
                    if isPalindrome(st[:i]):
                        curr.append(st[:i])
                        backtrack(curr, st[i:])
                        curr.pop()
        backtrack()
        return out
