class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for d in path.split('/'):
            if d == '..':
                if stack:
                    stack.pop()
            elif d not in ('', '.'):
                stack.append(d)
        out = ''
        for d in stack:
            out += '/' + d
        return out if stack else '/'
