# @algorithm @lc id=75 lang=python3 
# @title sort-colors


from en.Python3.mod.preImport import *
# @test([2,0,2,1,1,0])=[0,0,1,1,2,2]
# @test([2,0,1])=[0,1,2]
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dict_col = {0: 0, 1: 0, 2: 0}
        for num in nums:
            dict_col[num] += 1
        prev = 0
        for k, v in dict_col.items():
            nums[prev:(prev + v)] = [k] * v
            prev += v