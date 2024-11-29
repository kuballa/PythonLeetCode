# @algorithm @lc id=55 lang=python3 
# @title jump-game


from en.Python3.mod.preImport import *
# @test([2,3,1,1,4])=true
# @test([3,2,1,0,4])=false
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
