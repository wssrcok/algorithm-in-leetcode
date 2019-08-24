class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        d = {}
        for s in strs:
            temp = [0] * 26
            for c in s:
                temp[ord(c) - ord('a')] += 1
            temp = tuple(temp)
            if temp in d:
                out[d[temp]].append(s)
            else:
                d[temp] = len(out)
                out.append([s])

        return out
