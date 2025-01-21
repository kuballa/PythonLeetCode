# @algorithm @lc id=57 lang=python3 
# @title insert-interval


from en.Python3.mod.preImport import *
# @test([[1,3],[6,9]],[2,5])=[[1,5],[6,9]]
# @test([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])=[[1,2],[3,10],[12,16]]
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = ([min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])])
        if newInterval not in res:
            res.append(newInterval)
        return res if len(intervals) > 0 else [newInterval]