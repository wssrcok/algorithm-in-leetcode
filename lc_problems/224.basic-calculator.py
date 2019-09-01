#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
class Solution:
    def calculate(self, s: str) -> int:
        s = ''.join(s.split())
        stack = []
        j = len(s) - 1
        while j >= 0:
            if s[j].isdigit():
                i = j
                while i >= 0 and s[i].isdigit():
                    i -= 1
                stack.append(int(s[i+1:j+1]))
                j = i + 1
            elif s[j] == '(':
                _sum = stack.pop()
                op = stack.pop()
                while op != ')':
                    num = stack.pop()
                    assert(type(num) is int)
                    _sum += num if op == '+' else -num
                    op = stack.pop()
                stack.append(_sum)
            else:
                stack.append(s[j])
            j -= 1
        res = int(stack.pop())
        while stack:
            op, num = stack.pop(), stack.pop()
            assert(op == '+' or op == '-')
            assert(type(num) is int)
            res += num if op == '+' else -num
        return res





