class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        out_set = set()
        my_set = set()
        for i in range(len(s) - 9):
            dna = s[i:i+10]
            if dna in my_set:
                out_set.add(dna)
            else:
                my_set.add(dna)
        return list(out_set)
