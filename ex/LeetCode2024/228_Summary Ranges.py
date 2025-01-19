# @algorithm @lc id=228 lang=python3 
# @title summary-ranges


from en.Python3.mod.preImport import *
# @test([0,1,2,4,5,7])=["0->2","4->5","7"]
# @test([0,2,3,4,6,8,9])=["0","2->4","6","8->9"]
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            if start != nums[i]:
                ans.append(f"{start}->{nums[i]}")
            else:
                ans.append(f"{start}")
            
            i += 1
        return ans