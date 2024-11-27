# @algorithm @lc id=189 lang=python3 
# @title rotate-array

from en.Python3.mod.preImport import *
# @test([1,2,3,4,5,6,7],3)=[5,6,7,1,2,3,4]
# @test([-1,-100,3,99],2)=[3,99,-1,-100]
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])