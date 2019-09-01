class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        val = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                

