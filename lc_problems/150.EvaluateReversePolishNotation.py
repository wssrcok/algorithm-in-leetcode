class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def decode(op):
            
            if op.lstrip('-').isdigit():
                return int(op)
            right = decode(tokens.pop())
            left = decode(tokens.pop())
            return calc(left, op, right)

        def calc(l, op, r):
            return l + r if op == '+' else\
                   l - r if op == '-' else\
                   l * r if op == '*' else\
                   int(l / r)
        return decode(tokens.pop())
