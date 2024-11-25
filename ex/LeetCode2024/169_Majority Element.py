# @algorithm @lc id=169 lang=python3 
# @title majority-element


from typing import List
from en.Python3.mod.preImport import *
# @test([3,2,3])=3
# @test([2,2,1,1,1,2,2])=2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]