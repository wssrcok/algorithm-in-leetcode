from collections import Counter
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diff_is_one(w1, w2):
            diff = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    diff += 1
                if diff > 1:
                    return False
            return diff == 1

        def bfs():
            queue = collections.deque([(set(), beginWord, 1)])
            while queue:
                history, word, steps = queue.popleft()
                if word == endWord:
                    return steps
                for w in wordList:
                    if w not in history and diff_is_one(w, word):
                        my_history = history.copy()
                        my_history.add(w)
                        queue.append(my_history, w, steps+1)
            return 0
        return bfs

                        
                    
            
