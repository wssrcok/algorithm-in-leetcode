class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda a:a[0])
        out = [intervals[0]]
        for i in range(1, len(intervals)):
            if out[-1][0] <= intervals[i][1] and intervals[i][0] <= out[-1][1]:
                out[-1] = [min(out[-1][0], intervals[i][0]), max(out[-1][1], intervals[i][1])]
            else:
                out.append(intervals[i])
        return out
                
