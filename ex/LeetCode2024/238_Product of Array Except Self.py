# @algorithm @lc id=238 lang=python3 
# @title product-of-array-except-self

from en.Python3.mod.preImport import *
# @test([1,2,3,4])=[24,12,8,6]
# @test([-1,1,0,-3,3])=[0,0,9,0,0]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        pre = 1
        for x in range(len(nums)):
            output[x] *= pre
            pre *= nums[x]
        
        post = 1
        for x in range(len(nums) - 1, -1, -1):
            output[x] *= post
            post *= nums[x]
        
        return output