#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TreeNode(-1)

    def follow(self, word):
        cur = self.root
        i = 0
        while i < len(word) and word[i] in cur.children:
            cur = cur.children[word[i]]
            i += 1
        return cur  # the rest of words should be in cur

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.follow(word)
        while cur.index + 1 < len(word):
                i = cur.index + 1
                child = self.TreeNode(i)
                cur.children[word[i]] = child
                cur = child
        cur.word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.follow(word)
        return cur.index == len(word) - 1 and cur.word
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.follow(prefix)
        return cur.index == len(prefix) - 1

    class TreeNode(object):
        def __init__(self, index):
            self.index = index
            self.word = False
            self.children = {}
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

