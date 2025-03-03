# @algorithm @lc id=210 lang=python3 
# @title course-schedule-ii


from en.Python3.mod.preImport import *
# @test(2,[[1,0]])=[0,1]
# @test(4,[[1,0],[2,0],[3,1],[3,2]])=[0,2,1,3]
# @test(1,[])=[0]
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dict_cur = {i:[] for i in range(numCourses)}
        result = []
        visited = set()

        for i, j in prerequisites:
            dict_cur[j].append(i)
        
        def dfs(i):
            if i in visited:
                return False
            if dict_cur[i] == []:
                return True
            
            visited.add(i)
            for elem in dict_cur[i]:
                dfs(elem)
            visited.remove(i)
            dict_cur[i] = []
            result.append(i)
            return True

        for i in range(numCourses):
            if dfs(i):
                break

        return result