# @algorithm @lc id=80 lang=python3 
# @title remove-duplicates-from-sorted-array-ii


from typing import List
from en.Python3.mod.preImport import *
# @test([1,1,1,2,2,3])=5
# @test([0,0,1,1,1,1,2,3,3])=7
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[j] = nums[i]
                j += 1
            
        return j