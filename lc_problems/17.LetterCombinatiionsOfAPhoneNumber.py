class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        out = []
        m = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
             '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def dfs(i=0, letters=''):
            if len(digits) == i:
                out.append(letters)
            else:
                for c in m[digits[i]]:
                    dfs(i + 1, letters + c)
        dfs()
        return out
