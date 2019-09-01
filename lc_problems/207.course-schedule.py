#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ranks = {}
        m = {}
        for i in range(numCourses):
            ranks.setdefault(i, 0)
            m.setdefault(i, [])
        for [course, prereq] in prerequisites:
            m[prereq] += [course]
            ranks[course] += 1
        while True:
            q = collections.deque()
            for course in ranks:
                if ranks[course] == 0:
                    q.append(course)
            if not q: return False
            while q:
                prereq = q.popleft()
                for course in m.get(prereq, []):
                    ranks[course] -= 1
                del ranks[prereq]
            if not ranks: return True


        

