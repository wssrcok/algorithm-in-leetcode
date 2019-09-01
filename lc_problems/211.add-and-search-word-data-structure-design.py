#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#
class Trie:
    def __init__(self, index):
        self.index = index
        self.isEnd = False
        self.children = {}  # letter map to Trie

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie(-1)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for c in word:
            cur = cur.children.setdefault(c, Trie(cur.index + 1))
        cur.isEnd = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        s = [(self.root, 0)]
        while s:  # dfs
            cur, i = s.pop()
            if i == len(word): 
                if cur.isEnd:
                    return True  # is a word not prefix
            else:
                c = word[i]
                if c == '.':
                    for k in cur.children:
                        s.append((cur.children[k], i+1))
                elif c in cur.children:
                    s.append((cur.children[c], i+1))
        return False

        
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

