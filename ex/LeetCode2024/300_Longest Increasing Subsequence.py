# @algorithm @lc id=300 lang=python3 
# @title longest-increasing-subsequence


from en.Python3.mod.preImport import *
# @test([10,9,2,5,3,7,101,18])=4
# @test([0,1,0,3,2,3])=4
# @test([7,7,7,7,7,7,7])=1
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)