# @algorithm @lc id=207 lang=python3 
# @title course-schedule


from en.Python3.mod.preImport import *
# @test(2,[[1,0]])=true
# @test(2,[[1,0],[0,1]])=false
# @test(5, [[1,4],[2,4],[3,1],[3,2]])=true
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for i, j in prerequisites:
            preMap[i].append(j)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            
            visited.add(course)
            for elem in preMap[course]:
                if not dfs(elem): return False
            visited.remove(course)
            preMap[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True

        
            