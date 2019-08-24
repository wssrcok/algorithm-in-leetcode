from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        d = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if stack and c in d and stack[-1] == d[c]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
