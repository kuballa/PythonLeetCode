# @algorithm @lc id=219 lang=python3 
# @title contains-duplicate-ii


from en.Python3.mod.preImport import *
# @test([1,2,3,1],3)=true
# @test([1,0,1,1],1)=true
# @test([1,2,3,1,2,3],2)=false
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = {}

        for i in range(len(nums)):
            if nums[i] in num_map:
                if abs(i - num_map[nums[i]]) <= k:
                    return True
            num_map[nums[i]] = i

        return False