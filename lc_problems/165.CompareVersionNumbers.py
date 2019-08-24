class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        i = 0
        while i < min(len(version1), len(version2)):
            v1, v2 = int(version1[i]), int(version2[i])
            if v1 != v2:
                return 1 if v1 > v2 else -1
            i += 1
        while i < len(version1):
            if int(version1[i]) > 0:
                return 1
            i += 1
        while i < len(version2):
            if int(version2[i]) > 0:
                return -1
            i += 1
        return 0

