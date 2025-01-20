# @algorithm @lc id=56 lang=python3 
# @title merge-intervals


from en.Python3.mod.preImport import *
# @test([[1,3],[2,6],[8,10],[15,18]])=[[1,6],[8,10],[15,18]]
# @test([[1,4],[4,5]])=[[1,5]]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if lastEnd >= start:
                output[-1][1] = max(end, lastEnd)
            else:
                output.append([start, end])
        return output