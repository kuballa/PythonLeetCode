# @algorithm @lc id=39 lang=python3 
# @title combination-sum


from en.Python3.mod.preImport import *
# @test([2,3,6,7],7)=[[2,2,3],[7]]
# @test([2,3,5],8)=[[2,2,2,2],[2,3,3],[3,5]]
# @test([2],1)=[]
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return res