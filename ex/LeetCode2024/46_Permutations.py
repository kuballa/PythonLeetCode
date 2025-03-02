# @algorithm @lc id=46 lang=python3 
# @title permutations


from en.Python3.mod.preImport import *
# @test([1,2,3])=[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# @test([0,1])=[[0,1],[1,0]]
# @test([1])=[[1]]
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        
        result = []
        for i in range(len(nums)):
            n = nums[i]
            remaining = nums[:i] + nums[i+1:]  # Avoid modifying the list in place
            
            for perm in self.permute(remaining):
                result.append([n] + perm)
        
        return result