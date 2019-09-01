class Solution(object):
    def isMatch(self, text, pattern, mem = {}):
        if not pattern:
            return not text
        if (text, pattern) in mem:
            return mem[(text, pattern)]
        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            mem[(text, pattern)] = (self.isMatch(text, pattern[2:]) or  #  repeat 0 match
                    first_match and self.isMatch(text[1:], pattern))  # first match then continue matching
        else:
            mem[(text, pattern)] = first_match and self.isMatch(text[1:], pattern[1:])
        return mem[(text, pattern)]
