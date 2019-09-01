#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ranks = {}
        m = {}
        for i in range(numCourses):
            ranks.setdefault(i, 0)
            m.setdefault(i, [])
        for [course, prereq] in prerequisites:
            m[prereq] += [course]
            ranks[course] += 1
        res = []
        while True:
            q = collections.deque()
            for course in ranks:
                if ranks[course] == 0:
                    q.append(course)
            if not q: return []
            while q:
                prereq = q.popleft()
                for course in m.get(prereq, []):
                    ranks[course] -= 1
                del ranks[prereq]
                res.append(prereq)
            if not ranks: return res


        



