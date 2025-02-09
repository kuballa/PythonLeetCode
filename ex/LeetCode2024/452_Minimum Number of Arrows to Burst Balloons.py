# @algorithm @lc id=452 lang=python3 
# @title minimum-number-of-arrows-to-burst-balloons


from en.Python3.mod.preImport import *
# @test([[10,16],[2,8],[1,6],[7,12]])=2
# @test([[1,2],[3,4],[5,6],[7,8]])=4
# @test([[1,2],[2,3],[3,4],[4,5]])=2
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) < 1 or len(points[0]) < 1:
            return 0

        points.sort(key = lambda x: x[1])
        current_point = points[0]
        result = 1

        for point in points[1:]:
            if not (point[0] <= current_point[1] and point[1] >= current_point[0]):
                result += 1
                current_point = point
                
        return result